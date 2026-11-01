#!/usr/bin/env python3
"""Read-only, exact-image parser for original-Pro initialization/profile data.
No firmware execution, device I/O, patching or binary export. Python 3.10+.
The data decoder is a Python translation of the inspected startup decompressor,
not a CPU emulator. Register meaning and HDR capability are NOT inferred here.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import struct
from pathlib import Path

EXPECTED_SHA256 = '5f3965f20e2e468efb70c6e268f2b7b2743bce47e6ecfa999faadf2637c96228'
BIAS = 0x0800EFE8
POLY = 0xF4ACFB13
RAM_BASE = 0x20000000


def crc32_msb(data: bytes) -> int:
    crc = 0
    for value in data:
        crc ^= value << 24
        for _ in range(8):
            crc = ((crc << 1) ^ (POLY if crc & 0x80000000 else 0)) & 0xFFFFFFFF
    return crc


def decode_init(src: bytes, output_size: int) -> tuple[bytes, int]:
    if not 0 < output_size <= 0x10000:
        raise ValueError('Unsupported initialized-data size')
    out = bytearray()
    pos = 0
    def take() -> int:
        nonlocal pos
        if pos >= len(src):
            raise ValueError('Truncated compressed data')
        value = src[pos]
        pos += 1
        return value
    while len(out) < output_size:
        token = take()
        literals = token & 7
        if literals == 0:
            literals = take()
        repeat = token >> 4
        if repeat == 0:
            repeat = take()
        if literals == 0:
            raise ValueError('Invalid zero literal counter')
        literals -= 1
        if pos + literals > len(src) or len(out) + literals > output_size:
            raise ValueError('Literal run out of bounds')
        out.extend(src[pos:pos + literals])
        pos += literals
        if token & 8:
            distance = take()
            if not 1 <= distance <= len(out):
                raise ValueError('Invalid backreference')
            repeat += 2
            if len(out) + repeat > output_size:
                raise ValueError('Backreference out of bounds')
            for _ in range(repeat):
                out.append(out[-distance])
        else:
            if len(out) + repeat > output_size:
                raise ValueError('Zero run out of bounds')
            out.extend(bytes(repeat))
    return bytes(out), pos


def self_test() -> int:
    # Literal count is encoded as count+1. Backreferences may overlap.
    for encoded, expected in [
        (b'\x14ABC', b'ABC\0'),
        (b'\x04\x00ABC', b'ABC'),
        (b'\x21', b'\0\0'),
        (b'\x00\x04\x00ABC', b'ABC'),
        (b'\x2aA\x01', b'AAAAA'),
    ]:
        result, used = decode_init(encoded, len(expected))
        if result != expected or used != len(encoded):
            raise AssertionError('Decoder fixture failed')
    for encoded, size in [(b'', 1), (b'\x00\x00\x01', 1), (b'\x19\x01', 3), (b'\x21', 1)]:
        try:
            decode_init(encoded, size)
        except ValueError:
            pass
        else:
            raise AssertionError('Malformed fixture was accepted')
    return 9


def inspect(data: bytes) -> dict:
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError('Unknown stock image: parsing stopped')
    stored = struct.unpack_from('>I', data, 0)[0]
    length = struct.unpack_from('<I', data, 4)[0]
    computed = crc32_msb(data[8:])
    if length != len(data)-8 or stored != computed:
        raise ValueError('Container integrity mismatch')
    src_va, dest, size, decoder = struct.unpack_from('<4I', data, 0x24BD4)
    if (src_va, dest, size, decoder) != (0x08033BDC, RAM_BASE, 0xF68, 0x08010780):
        raise ValueError('Unexpected scatter-load record')
    initialized, consumed = decode_init(data[src_va-BIAS:], size)
    def read_at(va: int, length: int) -> bytes:
        if RAM_BASE <= va and va + length <= RAM_BASE + len(initialized):
            return initialized[va-RAM_BASE:va-RAM_BASE+length]
        off = va-BIAS
        if 24 <= off and off+length <= len(data):
            return data[off:off+length]
        raise ValueError(f'Unmapped profile address {va:#x}')
    def word_at(va: int) -> int:
        return struct.unpack('<I', read_at(va, 4))[0]
    profiles = []
    aggregate: dict[int, set[int]] = {}
    for row in range(5):
        for selector in range(1, 6):
            slot = RAM_BASE + 0xD0 + row*0x18 + selector*4
            ptr = word_at(slot)
            pairs = []
            for n in range(192):
                reg, value = read_at(ptr+2*n, 2)
                if reg == 0:
                    break
                pairs.append((reg, value))
                aggregate.setdefault(reg, set()).add(value)
            else:
                raise ValueError('Unterminated profile')
            profiles.append({
                'brightness_bucket': row, 'selector': selector,
                'pointer_slot': hex(slot), 'profile_address': hex(ptr),
                'pair_count': len(pairs), 'registers': [hex(r) for r,_ in pairs],
                'profile_sha256': hashlib.sha256(bytes(v for p in pairs for v in p)).hexdigest(),
            })
    return {
        'scope': 'static_original_pro_data_decode_not_device_measurement',
        'input_sha256': digest, 'input_bytes': len(data),
        'container_crc32_be': hex(stored), 'computed_crc32': hex(computed),
        'container_length_field': length,
        'container_identity': data[8:24].split(b'\0')[0].decode('ascii'),
        'initial_sp': hex(struct.unpack_from('<I',data,24)[0]),
        'reset_vector': hex(struct.unpack_from('<I',data,28)[0]),
        'payload_base': hex(BIAS+24), 'file_to_va_bias': hex(BIAS),
        'initialized_data_size': len(initialized), 'compressed_consumed': consumed,
        'compressed_source_offset': hex(src_va-BIAS),
        'compressed_end_offset': hex(src_va-BIAS+consumed),
        'initialized_data_sha256': hashlib.sha256(initialized).hexdigest(),
        'preset_index_map': [word_at(RAM_BASE+0x40+4*i) for i in range(5)],
        'brightness_values': list(struct.unpack('<9H',read_at(RAM_BASE+0x2E,18))),
        'profiles': profiles,
        'register_value_inventory': {
            hex(reg): {'distinct_count':len(values),'values_hex':[hex(v) for v in sorted(values)]}
            for reg, values in sorted(aggregate.items())},
        'warning': 'An MCU register/value command list is not a pixel lookup table. Meanings need exact-panel evidence. No HDR mode or capability is inferred.',
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('image', nargs='?', type=Path)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    fixtures = self_test()
    if args.image is None:
        if not args.self_test:
            parser.error('Provide an exact stock image, or --self-test')
        print(json.dumps({'decoder_fixtures_passed': fixtures}))
        return
    if args.image.stat().st_size > 2_000_000:
        parser.error('Input exceeds size limit')
    report = inspect(args.image.read_bytes())
    report['decoder_fixtures_passed'] = fixtures
    print(json.dumps(report, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
