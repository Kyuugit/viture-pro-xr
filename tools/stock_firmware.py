#!/usr/bin/env python3
"""Read-only stock-firmware acquisition/inspection. No USB, patching or flashing.

Historical hashes are provenance checks, not device compatibility or write approval.
The XREAL-style checksum is tested only as a format hypothesis for VITURE.
Python 3.10+, standard library only. Output directories must not already exist.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import struct
import sys
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

MANIFEST = 'https://static.viture.com/dfu-util/js/vers.js'
LIMIT = 8 * 1024 * 1024
KNOWN = {
    'N6P': '5f3965f20e2e468efb70c6e268f2b7b2743bce47e6ecfa999faadf2637c96228',
    'N6PL': '306e4b49849570da5fcd8e2933ad46a7e27848ec7733e0e0de8a783ba9c20dc5',
}

def crc_candidate(data: bytes) -> int:
    """XREAL container hypothesis: MSB-first, init/xorout 0, poly F4ACFB13."""
    crc = 0
    for byte in data:
        crc ^= byte << 24
        for _ in range(8):
            crc = ((crc << 1) ^ (0xF4ACFB13 if crc & 0x80000000 else 0)) & 0xFFFFFFFF
    return crc

def inspect(data: bytes) -> dict:
    if not 32 <= len(data) <= LIMIT:
        raise ValueError('Expected a 32-byte to 8-MiB local artifact.')
    if data.lstrip().lower().startswith((b'<!doctype', b'<html')):
        raise ValueError('This looks like an HTML page, not a firmware artifact.')
    digest = hashlib.sha256(data).hexdigest()
    length = struct.unpack_from('<I', data, 4)[0]
    exact_length = length == len(data) - 8
    crc = crc_candidate(data[8:]) if exact_length else None
    edids = []
    start = 0
    while True:
        pos = data.find(b'\x00\xff\xff\xff\xff\xff\xff\x00', start)
        if pos < 0:
            break
        block = data[pos:pos + 128]
        edids.append({'file_offset': hex(pos), 'complete_base_block': len(block) == 128,
                      'base_checksum_ok': len(block) == 128 and sum(block) % 256 == 0})
        start = pos + 1
    return {
        'bytes': len(data), 'sha256': digest,
        'historical_20261029_matches': [key for key, value in KNOWN.items() if value == digest],
        'word_at_04_le': length, 'length_minus_8_matches': exact_length,
        'words_at_18_le': [hex(x) for x in struct.unpack_from('<II', data, 0x18)],
        'xreal_crc_hypothesis': {
            'computed': None if crc is None else hex(crc),
            'matches_big_endian_word_at_00': crc is not None and crc == int.from_bytes(data[:4], 'big'),
            'matches_little_endian_word_at_00': crc is not None and crc == int.from_bytes(data[:4], 'little'),
        },
        'edid_header_candidates': edids,
        'warning': 'Not a component map, device dump, signature check, patch or flash-approval result. '
                   'EDID candidates may be inactive or runtime-modified templates.',
    }

def parse_manifest(data: bytes) -> dict:
    match = re.fullmatch(r'\s*(?:var|let|const)\s+firmware_vers\s*=\s*(\{.*\})\s*;?\s*',
                         data.decode('utf-8-sig'), re.S)
    if not match:
        raise ValueError('Unexpected manifest syntax; refusing to execute JavaScript.')
    result = json.loads(match.group(1))
    if not isinstance(result, dict):
        raise ValueError('Manifest must contain a JSON object.')
    return result

def get(url: str) -> bytes:
    def allowed(value: str) -> bool:
        parsed = urlparse(value)
        return parsed.scheme == 'https' and parsed.hostname in ('static.viture.com', 'static.viture.dev')
    if not allowed(url):
        raise ValueError('Only the known official static HTTPS origins are accepted.')
    with urlopen(Request(url, headers={'User-Agent': 'VitureProStockResearch/1.0'}), timeout=30) as response:
        if not allowed(response.url):
            raise ValueError('Unexpected download redirect; inspect it manually.')
        data = response.read(LIMIT + 1)
    if len(data) > LIMIT:
        raise ValueError('Download exceeds the analysis size limit.')
    return data

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    fetch = sub.add_parser('fetch', help='Download stock data only; no glasses connection needed.')
    fetch.add_argument('selector', choices=sorted(KNOWN))
    fetch.add_argument('--out', type=Path, required=True, help='New private directory; never overwritten.')
    local = sub.add_parser('inspect', help='Inspect a previously downloaded local artifact.')
    local.add_argument('path', type=Path)
    args = parser.parse_args()
    try:
        if args.action == 'inspect':
            if args.path.stat().st_size > LIMIT:
                raise ValueError('Local file exceeds the analysis size limit.')
            report = inspect(args.path.read_bytes())
        else:
            if args.out.exists():
                raise ValueError('Output path already exists; choose a new private directory.')
            manifest = get(MANIFEST)
            entry = parse_manifest(manifest).get(args.selector)
            if not isinstance(entry, dict) or not isinstance(entry.get('url'), str):
                raise ValueError('Selected manifest entry has no firmware URL.')
            url = urljoin('https://static.viture.com', entry['url'])
            data = get(url)
            report = inspect(data)
            report.update(selector_requested=args.selector, source_url=url, manifest_entry=entry,
                          manifest_sha256=hashlib.sha256(manifest).hexdigest(), device_access=False)
            args.out.mkdir(parents=True, exist_ok=False)
            (args.out / '.gitignore').write_text('*\n', encoding='utf-8')
            (args.out / 'stock.bin').write_bytes(data)
            (args.out / 'manifest.js').write_bytes(manifest)
            (args.out / 'report.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
        print(json.dumps(report, indent=2))
        return 0
    except (OSError, ValueError, KeyError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
