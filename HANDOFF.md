# Next-stage handoff — original VITURE Pro XR

Updated 2026-11-01. Start with [the decision](DECISION-20261101.md). This repository owns future implementation, experiments and decisions; [bin owns the supporting evidence history](https://github.com/Kyuugit/bin/tree/main/viture-pro-xr-hdr-refresh-20261029).

**State at handoff:** research and arithmetic are complete for this continuation; empirical work has not started. No installations, local enumeration, device writes, firmware updates/downgrades, purchases or external outreach have been performed or authorized by the research. Do not treat this plan as permission to perform them.

## Evidence to carry forward

Use [immutable research snapshot 1f312101161d279b00713ac3d8c4cab79962cbff](https://github.com/Kyuugit/bin/tree/1f312101161d279b00713ac3d8c4cab79962cbff/viture-pro-xr-hdr-refresh-20261029), especially [candidate cards](https://github.com/Kyuugit/bin/blob/1f312101161d279b00713ac3d8c4cab79962cbff/viture-pro-xr-hdr-refresh-20261029/CANDIDATES-20261101.md), [source ledger](https://github.com/Kyuugit/bin/blob/1f312101161d279b00713ac3d8c4cab79962cbff/viture-pro-xr-hdr-refresh-20261029/SOURCES-20261101.md), [new experiments](https://github.com/Kyuugit/bin/blob/1f312101161d279b00713ac3d8c4cab79962cbff/viture-pro-xr-hdr-refresh-20261029/EXPERIMENTS-20261101.md) and [self-review](https://github.com/Kyuugit/bin/blob/1f312101161d279b00713ac3d8c4cab79962cbff/viture-pro-xr-hdr-refresh-20261029/REVIEW-20261101.md).

The inherited [requirements](https://github.com/Kyuugit/bin/blob/1f312101161d279b00713ac3d8c4cab79962cbff/viture-pro-xr-hdr-refresh-20261029/REQUIREMENTS.md), [experiment proposal](https://github.com/Kyuugit/bin/blob/1f312101161d279b00713ac3d8c4cab79962cbff/viture-pro-xr-hdr-refresh-20261029/EXPERIMENT-PROPOSAL.md) and [record template](https://github.com/Kyuugit/bin/blob/1f312101161d279b00713ac3d8c4cab79962cbff/viture-pro-xr-hdr-refresh-20261029/TEST-RECORD-TEMPLATE.json) still apply. Do not repeat resolved mistakes: original Pro is not Pro2/Luma/Beast; Sony ECX343E data does not establish ECX348E precision; receiver support and 10-bit input do not prove native optical HDR; metadata/API success and ACK do not prove delivered output; CRC is not firmware authenticity or recovery.

## Ordered work packages

| ID | Work and dependency | Completion evidence | Stop or branch condition |
|---|---|---|---|
| S0 | Source-only acquisition and exact-model mapping; may proceed independently of hardware tests | Authorized firmware bytes with acquisition record/hash, bounded EDID/template analysis, model-selector and control-path findings | Missing bytes or unclear provenance stays a recorded blocker. Do not substitute a different model or run an updater to acquire evidence. |
| B0 | Preserve the actual original-Pro baseline before any environmental change; requires permission for the specific local reads | Sanitized exact configuration, original/effective EDID, stock active mode/format, link state where exposed, restore/reconnect record | Unidentified unit, unavailable restore or uncontrolled update prevents comparative claims. Unknown telemetry remains explicitly unknown. |
| H1 | Host HDR-content reference; depends on B0 and selected workload/application | Reproducible renderer settings, confirmed HDR source, matched-reference comparison and declared optical/latency uncertainty | Wrong source transfer, clipped capture or double mapping requires pipeline repair before judging the glasses. |
| R1 | Full-SBS transport and refresh campaign; depends on B0, approved host changes, rollback and both-eye frame observation | Active 3840×1080 timing/encoding plus both-eye unique-frame evidence and actual observation/reconnect windows | Abort on artifacts, abnormal heating, loss of control/restore or other predeclared limits. OS-only refresh is not success. |
| N1 | Native-PQ discrimination; depends on B0 and a harness with adequate control/observability | Fixed-input/signaling comparisons and optical transfer evidence, with upstream/wire uncertainty explicit | If PQ input cannot be established or host transforms cannot be separated, classify as inconclusive and return to source work. |
| P1 | Post-release-unlock precedents; source-led, no purchase/update prerequisite | Exact model/build, old/new support and source/output evidence, reproducible before/after optical findings where available | Menu presence, visual boost, repeated anecdotes or new-model specifications do not qualify a strict native unlock. |
| D1 | Review results against the declared goals and revise the decision | A decision record linked to immutable evidence, including negative/inconclusive outcomes | Do not silently replace an unsuccessful experiment with a different goal or erase the earlier conclusion. |

S0 can remain active while the owner selects B0/H1/R1 conditions. H1 and R1 should not simultaneously change rendering, link format and firmware: separate variables and restore the reference between comparisons. N1 is not a prerequisite for either useful host mapping or refresh work.

## S0 — Most useful remaining source work

Reacquire the public N6P/N6PL payloads or use authorized historical copies, compare their hashes with the 29 October acquisition record, and record exact access time/version. The continuation did not acquire new bytes, so do not claim its old offsets or hashes are newly validated.

Decode the checksum-valid EDID candidate and its bounded declared extension; separately classify the checksum-failing candidates. Do not repair a template and publish it as a measured device EDID. Trace references, selection logic, runtime patching and reachable colour/transfer/timing operations. N6P and N6PL are variants, not evidence of a temporal firmware regression. A useful output is a small table separating declared capability, selected template, runtime observations still needed and a concrete next capture question.

A candidate interface only advances toward implementation when the exact model, command semantics, persistence and recovery are understood. Preserve licensing and redistribution boundaries; publish source references, hashes, offsets and necessary analysis rather than proprietary payloads or private identifiers.

## B0 — Baseline and authorization boundary

Record the exact unit and firmware privately; publish only the required sanitized model/revision. Identify the GPU that actually owns the connector, OS/driver, complete USB-C/adapter/cable route, video versus USB-control availability, EDID provenance, requested and active timing, chroma/range/depth, and negotiated rate/lane/DSC/FEC when exposed. Distinguish original device EDID from overrides and cached/effective EDID.

Preserve any existing custom-mode definitions without assuming they reproduce the recalled 93/95 Hz behaviour. Establish a known-good restore/reconnect procedure and maintain an off-head test fixture for experimental timings. An inherited SDK support label is not an optical validation of this particular connection.

**Pro Neckband gate:** its guide describes a first-use glasses firmware update. Address that dependency before connecting it as a comparator. Offline use is not assumed to prevent cached updates. Record all firmware and software changes; no update, downgrade or persistent operation is part of this baseline by default.

## H1 — Choose the workload, then the implementation

For movies, establish the mpv/libplacebo reference using a known HDR10/PQ asset. Compare MPC Video Renderer on an available suitable Windows host as an independent player path. Add HLG and specific Dolby Vision profiles separately after the reference works; decoder/profile failures are not evidence of sink capability.

For a suitable Linux live-game workload, test Gamescope with a known HDR client before a chosen game. Expose client HDR support while retaining SDR output; the force-PQ-output and inverse-tone-mapping options answer different questions. Pin backend/WSI/Proton and application state. Verify who creates the left/right images; a compositor does not automatically produce stereo content.

For Windows live-content feasibility, OBS is a lower-code prototype. Establish a real unclipped HDR capture source, one intended mapping stage and the exact source/canvas/filter/projector path. A separately authorized virtual HDR source display may enable application output but does not make the Pro a native HDR sink. Unsupported or protected capture may remain unsupported; no bypass is proposed.

Measure matched reference white, peak, near-black/colour patches, clipping, gradients and frame pacing with declared uncertainty. Record near-eye fixture geometry, pupil alignment, patch size, brightness/preset/tint/diopter state, dwell and warm-up. A renderer's target-nits field is not a measurement. Define a latency budget before judging an interactive prototype. Test asymmetric eye highlights, scene cuts and any temporal dither at the actual display cadence; this is an artifact check, not a previously observed defect.

Build custom capture/libplacebo integration only when a concrete correctness, compatibility or latency need survives these tests. Nightfall's inspected HDR-stream handling and PSVR2 mapping reports are design references, not ready original-Pro implementations or evidence of native PQ support.

## R1 — Observe the link before changing timings

First capture stock direct-path state before/after SBS selection, reconnect and any already available, approved alternate topology. Determine whether an apparent limit follows link negotiation, GPU ownership, format, timing admission or a mode-transition failure. Do not apply the Beast project's active debugfs workaround as a generic Pro diagnostic.

Then vary refresh, blanking, chroma and bit depth one at a time from validated operation, maintaining the transmitted 3840×1080 raster. Use the arithmetic script to reject impossible uncompressed assumptions, not to generate a supposedly safe timing. Non-exclusion is not acceptance. DSC requires actual source/sink/driver support and negotiation; bridge capability or an EDID edit alone does not establish it, and it does not remove an internal panel/bridge-output clock limit.

Observe unique frame identities in both eyes, accounting for camera exposure, rolling shutter, display scanout/PWM/dither and blind intervals. Intended repeated movie frames must be separated from unexpected display repeats/skips; a low-frame-rate movie alone cannot qualify higher delivered refresh. Record actual duration, frame count and reconnect/warm-state conditions rather than claiming a universal stable maximum. No target value derived from the 93/95 Hz recollection is treated as a safe start or a ceiling.

## N1 — One harness, a localized question

Choose DXGI on a suitable Windows host or a minimal reviewed DRM/KMS harness on an existing suitable Linux host. Do not build both unless the first leaves a specific host-related ambiguity. Do not execute the historical IGT suite unchanged: bpc changes, EDID gates and suspend/DPMS cases can confound this experiment.

Separate transfer-pattern tests from fixed-encoded-framebuffer/signaling tests. Hold timing, depth, range and colour transforms fixed where possible. Record remaining GPU/driver/wire uncertainty. A host CRC can help localize a transformation but is not independent wire evidence.

Correct repeatable optical response with established input conditions can support native processing for that configuration. Incorrect response under verified PQ rejects correct handling in that tested state, not all possible firmware states. Refused modes or unverified signaling are inconclusive. Even a positive result does not prove native panel bit depth. Only a concrete, reversible, model-specific mechanism can justify later control-loader planning; no flash or recovery assumptions are carried forward.

## P1 — What a qualifying precedent must contain

Prioritize exact-model XREAL 1S/One-family reports, not transfer of 1 Pro+ specifications. Seek old/new build identifiers, original/effective EDID, actual source transfer and output state, and fixed-input before/after optical response. Determine whether AI HDR enhances SDR, processes PQ, or merely appears in a menu. Conflicting no-effect reports remain part of the evidence.

For Quest/Nightfall, pin which renderer was actually used and distinguish an incoming HDR stream from the submitted headset output. For PSVR2, require reproducible implementation and calibration evidence before adopting an experimental mapping. Classify these as native unlock, client/host mapping, enhancement or platform restoration. PSVR2's HDR-at-launch status disqualifies it from the strict shipped-without-HDR category.

## Records, ownership and publication

Future project files and result summaries belong here. A proposed convention is `results/<date>-<experiment-id>/` for sanitized configuration, procedure, observations and an interpretation; creating such a record is not evidence that a trial ran. Link bulky or supporting research snapshots in the existing bin folder. Avoid duplicating a mutable evidence packet without its commit identity.

Each record must separate **proposed**, **executed**, **measured**, **inferred**, **negative** and **inconclusive**. Include exact source/binary versions, permissions/changes, source content identity, active output state, optical setup and uncertainty, raw-evidence location, repetitions, aborts and restoration. Keep serials, local paths and unrelated USB traffic private. A failed retrieval or absent driver telemetry is not a hardware finding.

Promote a capability only after the relevant evidence gate passes. Preserve prior records and append corrections with reasons. The immediate decisions are workload/host, quality-versus-chroma and latency trade-offs, measurement access, and exact action authorization—not a commitment to firmware modification or a numerical refresh promise.
