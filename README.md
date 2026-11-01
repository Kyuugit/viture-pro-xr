# Original VITURE Pro XR — device-side extension

This repository owns decisions, future implementation and experiments for the **original VITURE Pro XR**. It is not a Pro 2, Luma or Beast firmware project. Supporting research stays in [the existing bin archive](https://github.com/Kyuugit/bin/tree/main/viture-pro-xr-hdr-refresh-20261029), including earlier evidence and corrections.

## Current direction — 1 November 2026

**Start with [firmware feasibility and next implementation work](FIRMWARE-FEASIBILITY-20261101.md).** The owner prefers extending the glasses themselves. Keep **GlassVR** as the target and its already-reported high-rate full-SBS route as the refresh starting point. Host HDR mapping is a reference/fallback, not the default destination.

The preferred development model is a **Pro-specific guarded patch/build system retaining the vendor firmware core**. XREAL's Air-family kit supplies the actual firmware-engineering precedent; Pro 2 work supplies a runtime-protocol discovery method, not a ready flasher. The new Pro/XREAL 24-byte-header relationship is an actionable offline hypothesis, not yet a verified checksum or deployment path.

There are two separate gates: whether a Pro-specific modification can be accepted, booted and recovered; and whether the installed hardware can perform the desired function. The bridge family documents HDR reception and micro-OLED technology can support HDR systems, but original-Pro PQ processing and panel-native precision remain unestablished. Firmware acceptance does not create a missing per-pixel processing block.

| Workstream | Current priority |
|---|---|
| Firmware extension | Validate exact-Pro artifact/component structure and the recorded checksum hypothesis; map updater/boot/recovery semantics; design a guarded local builder for one understood change. |
| Native HDR/PQ | Identify a real reachable bridge/panel transfer stage and its precision/ordering, then test controlled input against optical output. HDR EDID declarations are insufficient. |
| Full-SBS refresh | Reconstruct and reuse GlassVR's CRU/SBS/connection/firmware setup; refine it one variable at a time and qualify delivered frames in both eyes. Neither 95 Hz nor the owner's approximate recollection is a ceiling. |
| IMU resource use | Profile the known provider-lifetime question separately. Closing unused streams may reduce overhead but does not turn the MCU into a full-rate software HDR engine. |
| Host HDR rendering | Retain controlled mappings and patterns as comparison/fallback. A movie player does not replace the chosen GlassVR integration target. |

## Evidence and handoff

[Current feasibility document](FIRMWARE-FEASIBILITY-20261101.md) contains the proposed shipping model, alternatives, unresolved decisions and ordered work packages. It links the immutable [bin feasibility snapshot](https://github.com/Kyuugit/bin/tree/ffcb915eb988b52b3d5131d04a77473445a15ff0/viture-pro-xr-hdr-refresh-20261029), especially [firmware portability](https://github.com/Kyuugit/bin/blob/ffcb915eb988b52b3d5131d04a77473445a15ff0/viture-pro-xr-hdr-refresh-20261029/FIRMWARE-PORTABILITY-20261101.md) and [chipset/panel HDR evidence](https://github.com/Kyuugit/bin/blob/ffcb915eb988b52b3d5131d04a77473445a15ff0/viture-pro-xr-hdr-refresh-20261029/CHIPSET-PANEL-HDR-20261101.md).

The historical [device-first decision](DECISION-DEVICE-FIRST-20261101.md) and [GlassVR refresh correction](DECISION-GLASSVR-REFRESH-20261101.md) remain in force. The original [decision](DECISION-20261101.md) and [handoff](HANDOFF.md) retain useful tools and validation requirements, but their host-first priority is superseded. The [previous complete project index](https://github.com/Kyuugit/viture-pro-xr/blob/20e1d710f4a6f0c5d27e7c6239b43eb7d7781457/README.md) preserves the earlier navigation and chronology.

## Completion boundary

This is a researched firmware-development strategy, **not a shipped original-Pro firmware, proven HDR unlock or measured overclock**. The new pass inspected primary sources and executed three arithmetic assertions. It did not acquire fresh Pro bytes, validate the proposed checksum, build a firmware image, upload/flash a device, test recovery, measure optical response or benchmark IMU contention. Historical firmware hashes and other authors' tests retain their original provenance.

No source finding or plan authorizes installation, device writes, firmware changes, purchases or outreach. Future records must distinguish proposed, built, accepted, measured, negative and inconclusive outcomes, preserve exact versions and model identity, and link supporting evidence in bin. Keep proprietary firmware and private per-unit data out of public releases unless the relevant rights and scope have been established. A local patch builder and a hardware updater are separate deliverables with separate gates.
