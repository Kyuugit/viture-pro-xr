# Original VITURE Pro XR — device-side extension

This repository owns decisions, future implementation and experiments for the **original VITURE Pro XR**. It is not a Pro 2, Luma or Beast firmware project. Supporting research stays in [the existing bin archive](https://github.com/Kyuugit/bin/tree/main/viture-pro-xr-hdr-refresh-20261029), including earlier evidence and corrections.

## Native HDR requirement — clarified 1 November 2026

**Read [the native-HDR requirement correction](NATIVE-HDR-REQUIREMENT-20261101.md) first.** The objective is genuine HDR input displayed by the glasses' native hardware, enabled/configured through the original-Pro STM32 firmware—not SDR-to-HDR enhancement, a host-mapped SDR substitute or a new MCU software pixel mapper. The STM32 is the firmware/control entry point; native HDR support in the exact bridge/panel configuration remains to be established.

The earlier MCU cycles-per-pixel argument addressed a different proposed architecture. It does not argue against configuring an existing native HDR mode through STM32 firmware. Prioritize tracing STM32 display initialization, bridge/panel configuration and reachable native transfer modes. Changes to bridge firmware may also be required; do not assume that an STM32-only change suffices. This clarification takes precedence over fallback/conversion suggestions in earlier feasibility documents.

## Development direction — 1 November 2026

Use [firmware feasibility and next implementation work](FIRMWARE-FEASIBILITY-20261101.md) subject to the requirement above. The owner prefers extending the glasses themselves. Keep **GlassVR** as the target and its already-reported high-rate full-SBS route as the refresh starting point. Host patterns and mapping tools may serve as test references; they do not satisfy or replace the native-HDR objective.

The preferred development model is a **Pro-specific guarded patch/build system retaining the vendor firmware core**. XREAL's Air-family kit supplies the actual firmware-engineering precedent; Pro 2 work supplies a runtime-protocol discovery method, not a ready flasher. The new Pro/XREAL 24-byte-header relationship is an actionable offline hypothesis, not yet a verified checksum or deployment path.

There are two separate gates: whether a Pro-specific modification can be accepted, booted and recovered; and whether the installed hardware can perform the desired function. The bridge family documents HDR reception and micro-OLED technology can support HDR systems, but original-Pro PQ processing and panel-native precision remain unestablished. Firmware acceptance alone does not establish the desired capability.

| Workstream | Current priority |
|---|---|
| Firmware extension | Validate exact-Pro artifact/component structure and the recorded checksum hypothesis; map updater/boot/recovery semantics; design a guarded local builder for one understood change. |
| Native HDR/PQ | Trace STM32-controlled bridge/panel initialization and any native HDR/transfer mode; establish its actual internal format and precision, then verify genuine HDR input against optical output. Do not substitute SDR enhancement or software pixel mapping. |
| Full-SBS refresh | Reconstruct and reuse GlassVR's CRU/SBS/connection/firmware setup; refine it one variable at a time and qualify delivered frames in both eyes. Neither 95 Hz nor the owner's approximate recollection is a ceiling. |
| IMU resource use | Profile the known provider-lifetime question separately. Measure actual shared-resource effects; MCU-per-pixel arithmetic is not a native-HDR enablement test. |
| Host HDR rendering | Retain controlled patterns/mappings as diagnostic comparisons only for this native-HDR goal. A movie player does not replace the chosen GlassVR integration target. |

## Evidence and handoff

[Current feasibility document](FIRMWARE-FEASIBILITY-20261101.md) contains the proposed shipping model, alternatives, unresolved decisions and ordered work packages, with scope clarified by [the native-HDR requirement](NATIVE-HDR-REQUIREMENT-20261101.md). It links the immutable [bin feasibility snapshot](https://github.com/Kyuugit/bin/tree/ffcb915eb988b52b3d5131d04a77473445a15ff0/viture-pro-xr-hdr-refresh-20261029), especially [firmware portability](https://github.com/Kyuugit/bin/blob/ffcb915eb988b52b3d5131d04a77473445a15ff0/viture-pro-xr-hdr-refresh-20261029/FIRMWARE-PORTABILITY-20261101.md) and [chipset/panel HDR evidence](https://github.com/Kyuugit/bin/blob/ffcb915eb988b52b3d5131d04a77473445a15ff0/viture-pro-xr-hdr-refresh-20261029/CHIPSET-PANEL-HDR-20261101.md).

The historical [device-first decision](DECISION-DEVICE-FIRST-20261101.md) and [GlassVR refresh correction](DECISION-GLASSVR-REFRESH-20261101.md) remain in force. The original [decision](DECISION-20261101.md) and [handoff](HANDOFF.md) retain useful tools and validation requirements, but their host-first priority is superseded. The [previous complete project index](https://github.com/Kyuugit/viture-pro-xr/blob/20e1d710f4a6f0c5d27e7c6239b43eb7d7781457/README.md) preserves the earlier navigation and chronology.

## Completion boundary

This is a researched firmware-development strategy, **not a shipped original-Pro firmware, proven HDR unlock or measured overclock**. The feasibility pass inspected primary sources and executed three arithmetic assertions; the subsequent requirement clarification did not run a new experiment. It did not acquire fresh Pro bytes, validate the proposed checksum, build a firmware image, upload/flash a device, test recovery, measure optical response or benchmark IMU contention. Historical firmware hashes and other authors' tests retain their original provenance.

No source finding or plan authorizes installation, device writes, firmware changes, purchases or outreach. Future records must distinguish proposed, built, accepted, measured, negative and inconclusive outcomes, preserve exact versions and model identity, and link supporting evidence in bin. Keep proprietary firmware and private per-unit data out of public releases unless the relevant rights and scope have been established. A local patch builder and a hardware updater are separate deliverables with separate gates.
