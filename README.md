# Original VITURE Pro XR — HDR presentation and full-SBS refresh

This is the project home for decisions, implementation and future testing of the **original VITURE Pro XR**. It is not a Pro 2, Luma or Beast project. Supporting research stays in [the existing bin evidence archive](https://github.com/Kyuugit/bin/tree/main/viture-pro-xr-hdr-refresh-20261029); do not move or overwrite its history.

## Current direction — 1 November 2026

**Build useful host-side HDR-content presentation first, qualify full-resolution SBS refresh in parallel, and keep native PQ processing as a bounded investigation rather than a prerequisite.** This is a recommendation from source research, not a demonstrated unlock or overclock.

Read the [consolidated decision and alternatives](DECISION-20261101.md), then the [next-stage handoff](HANDOFF.md). The decision is ready for owner selection of workload, host and test boundaries; it does not authorize installations, device writes, firmware changes, purchases or outreach.

| Separate goal | Current recommended path |
|---|---|
| Better presentation of HDR content | mpv/libplacebo for a controlled movie reference; Gamescope HDR-client-to-SDR-output for a suitable Linux gaming workload. Windows alternatives are MPC Video Renderer for movies and an OBS capture/projector feasibility prototype for live content. |
| Native HDR/PQ input and processing | One controlled DXGI or minimal DRM/KMS harness, plus source-only firmware/EDID investigation. Receiver HDR10 support is not proof of a native PQ-to-panel processing path. |
| Higher real per-eye refresh at 3840×1080 SBS | Establish actual link, format and mode-transition behaviour before timing/chroma experiments or firmware work. Optical frame identities in both eyes are required. |
| Headsets gaining HDR after release | Follow exact-model XREAL AI HDR reports, distinguish Nightfall client mapping and PSVR2 platform restoration, and require stronger evidence before calling any of them a strict native-HDR unlock. |

## Evidence and completion boundary

The [2026-11-01 research snapshot](https://github.com/Kyuugit/bin/tree/1f312101161d279b00713ac3d8c4cab79962cbff/viture-pro-xr-hdr-refresh-20261029) contains the continuation findings, candidate cards, source ledger, discriminating experiments and same-author review, alongside the preserved 29 October packet and its independent reviews. New arithmetic passed **10 fixed checks and 140 Decimal rechecks**. These are calculations, not display measurements.

**No new device measurements, accepted modes, native-PQ result, panel-precision proof, firmware recovery test or measured refresh maximum exists in this continuation.** The recalled approximately 93/95 Hz behaviour is not a verified ceiling. Fresh firmware retrieval did not complete; historical hashes remain historical acquisition evidence.

Future implementation, experiment records and decisions belong here. Link each result to its exact model/build/host configuration and supporting evidence in bin. Keep raw identifiers private, distinguish requested modes from active and optically delivered output, and record negative and inconclusive outcomes as well as successes.
