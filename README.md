# Original VITURE Pro XR — HDR presentation and full-SBS refresh

This is the project home for decisions, implementation and future testing of the **original VITURE Pro XR**. It is not a Pro 2, Luma or Beast project. Supporting research stays in [the existing bin evidence archive](https://github.com/Kyuugit/bin/tree/main/viture-pro-xr-hdr-refresh-20261029); do not move or overwrite its history.

## Current direction — device-side extension preferred

**Start with [the device-first decision and work packages](DECISION-DEVICE-FIRST-20261101.md).** The owner prefers extending the glasses themselves. This supersedes the initial host-mapping-first priority while retaining GlassVR as the integration target and its reported high-rate path as the refresh starting point. Host HDR mapping remains a comparison/fallback, not the default destination.

The strongest new firmware reference is a guarded, paired bridge/MCU patch kit for XREAL Air-family glasses using the LT7911UXC bridge family. It reports full-SBS and native-RGB improvements; it is **not a VITURE port or an HDR unlock**. The same follow-up identifies a GlassVR provider-lifetime issue worth profiling: selecting an external pose source may leave native IMU services active. Neither device-side nor host-side IMU contention has been measured. [Pinned evidence and review](https://github.com/Kyuugit/bin/blob/e50f9b80e7e2ffcfcc43941d80d3b70e25c89ba3/viture-pro-xr-hdr-refresh-20261029/FIRMWARE-EXTENSION-20261101.md).

Prioritize original-Pro artifact/component mapping, the GlassVR-motivated same-selector firmware-version comparison, and actual bridge/panel transfer controls. Transfer mechanisms from the XREAL work, never its firmware images or register offsets. No flashing, downgrade, installation or device test is authorized or claimed by this decision.

## Retained correction — GlassVR first for refresh

**Read [the corrected refresh decision and handoff](DECISION-GLASSVR-REFRESH-20261101.md).** It supersedes the refresh prioritization in the original decision/handoff below. The continuation missed the GlassVR author's archived original-Pro CRU setup instructions and firsthand 95 Hz SBS report. The first refresh task is to reconstruct and reuse that existing setup, then test its connection, timing and firmware-version dependencies—not restart a generic survey.

The recovered guide specifies CRU-added 3840×1080/90 after entering SBS; the author separately reports 95 Hz operation and improved stability with older firmware. CRU changes the host's EDID override, not the glasses' firmware. GlassVR's rendering cadence and physical display timing are separate. This is documented setup plus firsthand reported success, not a new independent optical measurement or proof that GlassVR patches firmware. [Supporting evidence and review](https://github.com/Kyuugit/bin/blob/8d40123f6432da4cb6bb12a430573fd8914764f7/viture-pro-xr-hdr-refresh-20261029/GLASSVR-REFRESH-CORRECTION-20261101.md).

## Earlier direction — retained as history, superseded in priority

The earlier recommendation was to **build useful host-side HDR-content presentation, qualify the existing GlassVR high-rate full-SBS path in parallel, and keep native PQ processing as a bounded investigation rather than a prerequisite.** The device-first addendum above changes that project priority at the owner's request and in light of stronger firmware evidence. The goals remain separate, and GlassVR remains the integration target.

Read the [original consolidated decision and alternatives](DECISION-20261101.md) and [original next-stage handoff](HANDOFF.md) with both addenda. They retain useful tools and validation requirements, but their host-first priority is no longer current. None of these documents authorizes installations, device writes, firmware changes, purchases or outreach.

| Separate goal | Current recommended path |
|---|---|
| Extend the glasses / native HDR-PQ investigation | Map exact-Pro firmware components, reachable color/transfer controls and coordinated bridge/panel profiles. Use the XREAL kit as a mechanism reference, not a binary to flash. Native PQ and panel precision remain distinct unknowns. |
| Higher real per-eye refresh at 3840×1080 SBS | Reconstruct the GlassVR author's CRU/SBS/DP setup first. Refine timing/format/connection dependencies and identify the reported firmware-version pair. Qualify both-eye delivery; 95 Hz is not a ceiling. |
| Better presentation of HDR content | Retain calibrated host mapping and controlled renderers as reference/fallback. A movie-player result does not establish GlassVR HDR integration. |
| IMU resource use | Check GlassVR provider lifetime and measure native IMU enabled versus genuinely closed with other variables fixed. Do not assume reduced IMU work creates video-processing capacity. |
| Headsets gaining HDR after release | Keep the strict native-unlock question open. The XREAL kit is genuine custom display-firmware work but not a demonstrated PQ unlock; previously identified software mapping/platform-restoration cases remain separately classified. |

## Evidence and completion boundary

The [initial 2026-11-01 research snapshot](https://github.com/Kyuugit/bin/tree/1f312101161d279b00713ac3d8c4cab79962cbff/viture-pro-xr-hdr-refresh-20261029) contains the continuation findings, candidate cards, source ledger, discriminating experiments and same-author review, alongside the preserved 29 October packet and its independent reviews. New arithmetic passed **10 fixed checks and 140 Decimal rechecks**. These are calculations, not display measurements. The subsequent GlassVR and device-first addenda are linked above and do not silently rewrite that snapshot.

**No new device measurements, accepted-mode tests, native-PQ result, panel-precision proof, firmware recovery test, IMU benchmark or measured refresh maximum were performed in this research.** That must not be confused with an absence of existing original-Pro high-rate reports: the GlassVR author's reported success is explicitly incorporated. The owner's recalled approximately 93/95 Hz behaviour and the author's report are separate records, neither a verified ceiling. Fresh firmware retrieval did not complete in the initial continuation; historical hashes remain historical acquisition evidence. The XREAL builders were inspected, not executed or ported.

Future implementation, experiment records and decisions belong here. Link each result to its exact model/build/host configuration and supporting evidence in bin. Keep raw identifiers private, distinguish requested modes from active and optically delivered output, and record negative and inconclusive outcomes as well as successes.
