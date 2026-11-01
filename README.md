# Original VITURE Pro XR — HDR presentation and full-SBS refresh

This is the project home for decisions, implementation and future testing of the **original VITURE Pro XR**. It is not a Pro 2, Luma or Beast project. Supporting research stays in [the existing bin evidence archive](https://github.com/Kyuugit/bin/tree/main/viture-pro-xr-hdr-refresh-20261029); do not move or overwrite its history.

## Current correction — GlassVR first for refresh

**Read [the corrected refresh decision and handoff](DECISION-GLASSVR-REFRESH-20261101.md) first.** It supersedes the refresh prioritization in the original decision/handoff below. The continuation missed the GlassVR author's archived original-Pro CRU setup instructions and firsthand 95 Hz SBS report. The first refresh task is now to reconstruct and reuse that existing setup, then test its connection, timing and firmware-version dependencies—not restart a generic survey.

The recovered guide specifies CRU-added 3840×1080/90 after entering SBS; the author separately reports 95 Hz operation and improved stability with older firmware. CRU changes the host's EDID override, not the glasses' firmware. GlassVR's rendering cadence and physical display timing are separate. This is documented setup plus firsthand reported success, not a new independent optical measurement or proof that GlassVR patches firmware. [Supporting evidence and review](https://github.com/Kyuugit/bin/blob/8d40123f6432da4cb6bb12a430573fd8914764f7/viture-pro-xr-hdr-refresh-20261029/GLASSVR-REFRESH-CORRECTION-20261101.md).

## Current direction — 1 November 2026

**Build useful host-side HDR-content presentation, qualify the existing GlassVR high-rate full-SBS path in parallel, and keep native PQ processing as a bounded investigation rather than a prerequisite.** These are separate workstreams. The choice of GlassVR as the integration target is retained from the earlier research.

Read the [consolidated decision and alternatives](DECISION-20261101.md) and [original next-stage handoff](HANDOFF.md) together with the correction above. The correction takes precedence for refresh. These documents do not authorize installations, device writes, firmware changes, purchases or outreach.

| Separate goal | Current recommended path |
|---|---|
| Better presentation of HDR content | mpv/libplacebo for a controlled movie reference; Gamescope HDR-client-to-SDR-output for a suitable Linux gaming workload. Windows alternatives are MPC Video Renderer for movies and an OBS capture/projector feasibility prototype for live content. |
| Native HDR/PQ input and processing | One controlled DXGI or minimal DRM/KMS harness, plus source-only firmware/EDID investigation. Receiver HDR10 support is not proof of a native PQ-to-panel processing path. |
| Higher real per-eye refresh at 3840×1080 SBS | Reconstruct the GlassVR author's CRU/SBS/DP setup first. Refine its timing/format/connection dependencies and identify the reported firmware-version pair. Qualify actual frame delivery in both eyes; do not treat 95 Hz as a ceiling. |
| Headsets gaining HDR after release | Follow exact-model XREAL AI HDR reports, distinguish Nightfall client mapping and PSVR2 platform restoration, and require stronger evidence before calling any of them a strict native-HDR unlock. |

## Evidence and completion boundary

The [initial 2026-11-01 research snapshot](https://github.com/Kyuugit/bin/tree/1f312101161d279b00713ac3d8c4cab79962cbff/viture-pro-xr-hdr-refresh-20261029) contains the continuation findings, candidate cards, source ledger, discriminating experiments and same-author review, alongside the preserved 29 October packet and its independent reviews. New arithmetic passed **10 fixed checks and 140 Decimal rechecks**. These are calculations, not display measurements. The subsequent GlassVR correction is linked above and does not silently rewrite that snapshot.

**No new device measurements, accepted-mode tests, native-PQ result, panel-precision proof, firmware recovery test or measured refresh maximum were performed in this research.** That must not be confused with an absence of existing original-Pro high-rate reports: the GlassVR author's reported success is now explicitly incorporated. The owner's recalled approximately 93/95 Hz behaviour and the author's report are separate records, neither a verified ceiling. Fresh firmware retrieval did not complete in the initial continuation; historical hashes remain historical acquisition evidence.

Future implementation, experiment records and decisions belong here. Link each result to its exact model/build/host configuration and supporting evidence in bin. Keep raw identifiers private, distinguish requested modes from active and optically delivered output, and record negative and inconclusive outcomes as well as successes.
