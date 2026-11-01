# Corrected refresh decision and handoff: reuse GlassVR first

Date: 2026-11-01. This addendum supersedes the refresh prioritization in [DECISION-20261101.md](DECISION-20261101.md) and the R1/S0 refresh tasks in [HANDOFF.md](HANDOFF.md). Other goal-specific findings and safeguards remain in force. The correction follows the owner's valid objection that the continuation did not properly reuse the GlassVR research.

## Decision

**The leading refresh workstream is to reconstruct, reproduce and improve the GlassVR author's existing original-VITURE-Pro high-rate SBS setup, not to restart a generic search for how to exceed 60 Hz.** Keep GlassVR as the intended integration target. A small standalone renderer is an isolation tool, not an unsolicited replacement for it.

[Immutable supporting correction and source review in bin](https://github.com/Kyuugit/bin/blob/8d40123f6432da4cb6bb12a430573fd8914764f7/viture-pro-xr-hdr-refresh-20261029/GLASSVR-REFRESH-CORRECTION-20261101.md) records the recovered instructions, direct author reports, implementation boundaries and confidence. The prior [GlassVR source review](https://github.com/Kyuugit/bin/blob/main/glassvr-pro-xr-desktop-20261029/GLASSVR-SOURCE.md) remains the integration foundation.

## Established starting point

The upstream archived guide at the previously reviewed commit describes **original Pro full-SBS 3840×1080/60 → CRU-added 3840×1080/90 → graphics-driver restart**. The author separately reports **95 Hz SBS working in SteamVR**, success through a DP adapter, and improved stability after a firmware downgrade. The archived guide is still in the current tree as `media/old README.md`; it was not necessary to rediscover the problem from scratch.

The evidence supports a host EDID/timing override and connection/firmware-version dependencies. CRU changes Windows registry EDID overrides, not the glasses' firmware. The inspected GlassVR code sets stereo geometry and OpenVR refresh/pacing and uses the VITURE SDK for tracking; the inspected connection path does not establish an automatic firmware patch or 95 Hz device-programming operation. Do not conflate configuring SteamVR cadence with configuring the physical display mode.

Classify this as a **documented method plus firsthand reported working original-Pro setup**. Missing independent optical qualification does not demote it to a mere recollection or generic speculation. It does prevent calling 95 Hz a measured universal result, a safe default, or a ceiling. The guide's 90 Hz procedure and the separate 95 Hz report must remain distinct until the exact latter timing is recovered.

## Revised priorities

| Rank | Work | Why now |
|---|---|---|
| 1 | Recover the GlassVR author's exact high-rate setup and reuse it | Strongest exact-model practical evidence, directly connected to the intended application. |
| 2 | Refine that baseline's timing, output format and connection path | Tests which dependency accounts for admission, stereo splitting, stability and real delivery rather than guessing a limit. |
| 3, parallel source lane | Identify and compare the firmware versions associated with the author's report | Concrete original-Pro motivation; more actionable than speculative DSC. No downgrade is assumed necessary or authorized. |
| 4, conditional | Investigate DSC or internal bridge/panel changes | Only after the existing path leaves a specific unexplained bottleneck. |

The host-HDR and native-PQ lanes stay separate. High-rate timing success is not HDR processing proof. Source-only firmware work should now specifically pursue the version pair behind this report, rather than comparing N6P and N6PL variants as though they were successive releases.

## Immediate source work — no hardware prerequisite

Recover the linked `hz2.png` settings evidence and any original CRU export; identify exact timings, output chroma/depth/range, successful firmware identifiers, GPU/driver and DP adapter. The correction did not visually inspect that image, so neither approximately 420 MHz nor 4:2:2/8-bit is newly verified by it. Preserve unknown fields instead of substituting another model's EDID.

Trace the relationship between physical SBS selection, host EDID override, actual mode selection, GlassVR geometry and its refresh field. The existing review already establishes 1920×1080 per-eye settings and doubled SBS width; do not redo unrelated tracking/controller research. Maintain links to immutable upstream versions and separate the author's report from measured reproduction.

## Next authorized bench work — isolate the mechanism

First preserve the installed firmware and original/effective EDID, existing custom modes, connection and rollback. Do not update or downgrade firmware before recording this baseline. The historical guide's GPU-driver-uninstall advice is not the default recovery procedure; use a reviewed override-removal/restore plan based on CRU's own documentation.

Then compare the same full-SBS physical mode in a simple frame-coded renderer and in GlassVR. Keep timing, firmware, format, brightness and connection fixed. Observe each eye independently. If both work, the physical-mode enabling is not dependent on GlassVR's stereo renderer; GlassVR remains the intended SteamVR application path. If only one works, examine mode-switch order, runtime controls, presentation and pacing before inventing a firmware patch mechanism.

Compare an already available approved alternate connection at fixed settings. If adapter choice changes mode admission or the SBS split, localize the connection/negotiation issue; do not call a mirrored 3840×1080 image successful stereo. Verify selected versus optically delivered refresh and restoration separately.

Only after exact firmware identification, relevant recovery evidence and separate authorization should firmware-version A/B be considered. Hold connection and timing constant. A changed result implicates version-dependent behavior; it still does not identify a particular internal limit without further evidence. Source comparison may continue before that hardware decision.

## Correction acceptance and remaining decisions

The research correction is complete when the current index points to this decision and the bin source record, with the previous refresh ranking explicitly superseded. Experimental success remains future work: a reproduced full-raster mode, correct eye splitting, distinct frames in both eyes and declared observation duration/uncertainty.

The owner need not reselect GlassVR or re-explain the high-rate lead. Remaining decisions concern the exact local test scope, acceptable chroma trade-off, observation equipment and any later firmware experiment. This correction authorizes none of those device actions and reports no new measurement. Future implementation and results belong here; evidence and historical corrections stay in the existing bin folder.
