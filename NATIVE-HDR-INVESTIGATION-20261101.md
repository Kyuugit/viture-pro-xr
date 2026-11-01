# Native-HDR investigation: concrete control pathways and next work

Date: 2026-11-01. Status: source research and engineering recommendation, not a firmware release or native-HDR demonstration. [The native-HDR requirement](NATIVE-HDR-REQUIREMENT-20261101.md) remains authoritative: genuine HDR input displayed by the original Pro's native hardware, enabled through STM32/device configuration. No SDR enhancement or software pixel mapper is proposed. GlassVR remains the integration target, and its existing reported high-rate SBS route remains the refresh baseline lead.

## Decision from the new research

**Start with the original Pro's stock colour-preset/panel-initialization control path, not an assumed HDR-enable bit or the Pro 2 tracking driver.** VITURE explicitly says Pro 2 tunes the Sony panel's gamma through panel registers. Original Pro already has on-device, firmware-dependent colour presets. This is a concrete, higher-value way to locate native display controls. It does not prove the controls can provide PQ operation.

Use Luma Pro as an additional family comparison: the official colour tool supports it, and the SDK groups it with original Pro under Gen1. Pro 2 is Gen2 and Luma Ultra is Carina. These distinctions help select source comparisons; none establishes transferable opcodes or identical panels.

Use the XREAL kit as a reference for firmware-enabled panel readback and coordinated bridge/panel setup. It provides more than a generic firmware writer, but its diagnostic response validation has specific shortcomings. Any Pro implementation must be separately designed and verified rather than copied unchanged.

## Published supporting evidence

Research and history remain in bin. The immutable [478f406996d07701e07b2c6456997243c9d33eb4 snapshot](https://github.com/Kyuugit/bin/tree/478f406996d07701e07b2c6456997243c9d33eb4/viture-pro-xr-hdr-refresh-20261029) contains:

- [Native-HDR pathway evidence and ranked candidates](https://github.com/Kyuugit/bin/blob/478f406996d07701e07b2c6456997243c9d33eb4/viture-pro-xr-hdr-refresh-20261029/NATIVE-HDR-PATHWAYS-20261101.md).
- [Source review and diagnostic validation gaps](https://github.com/Kyuugit/bin/blob/478f406996d07701e07b2c6456997243c9d33eb4/viture-pro-xr-hdr-refresh-20261029/NATIVE-HDR-PATHWAYS-REVIEW-20261101.md).

These supplement the earlier [firmware feasibility](FIRMWARE-FEASIBILITY-20261101.md), [device-first decision](DECISION-DEVICE-FIRST-20261101.md) and [GlassVR correction](DECISION-GLASSVR-REFRESH-20261101.md). They do not replace original evidence or claim a new independent review.

## What actually became more concrete

| Finding | Consequence | Limit |
|---|---|---|
| Manufacturer-described Pro 2 panel-register gamma tuning | Promote panel/preset handler analysis, rather than treating Pro 2 only as a host-protocol reference | No documented original-Pro PQ mode or arbitrary transfer-table capacity yet |
| Original-Pro preset selection and official MCU-then-DP update description | Gives an exact-model operation and motivates paired component mapping | Doesn't identify the processing location or prove custom firmware acceptance |
| XREAL MCU diagnostic and paired panel/bridge changes | Gives a practical instrumentation/coordination design | Patched Air-only mechanism; not a stock Pro command or HDR result |
| Sony ECX335SN diagram contains native gamma hardware and mixed-depth stages | Directs the exact-panel manual search toward native transfer controls and precision boundaries | Different panel; ten-bit intermediates followed by eight-bit output do not prove Pro precision |
| Exact LT7911UXC-family code exposes an HDR-related receiver state | Gives a concrete receiver-observability mechanism to correlate with the Pro STM32 control loop | A firmware-specific capture-board status is not an HDR-enable bit or native optical response |

## Ordered source and implementation work

### N0 — Build an exact-Pro display-control map

Use legitimately obtained, hash-identified Pro MCU/DP artifacts. Trace the existing physical colour-preset selection and display initialization to their function/table consumers. Record whether each operation targets the bridge, one or both panels, nonvolatile settings, or a host-only interface. Map known reset/init and stock preset operations before adding any new operation.

For source search, use the actual preset strings/tables, transaction structure and caller relationships; do not infer semantics from matching bytes alone. The previous Pro/XREAL container-checksum relationship remains an untested hypothesis. Missing artifacts are a source-access gap, not a reason to invent a map.

**Output:** a small annotated control map with exact image hashes, offsets/function evidence, target bus and observed-versus-inferred semantics. If a preset only changes gain or temperature, record that narrower result.

### N1 — Resolve native panel capability before proposing an HDR patch

Identify the fitted panel suffix and its programming documentation. Determine whether native PQ is a selectable mode, whether existing hardware transfer resources can represent the required HDR response, and what input/internal precision and operating conditions apply. Distinguish fixed SDR calibration controls from a native HDR-capable transfer mechanism. Do not design an SDR enhancement curve or introduce a software conversion fallback as success.

**Output:** a capability verdict tied to exact registers and the installed part. If only one route is excluded, say which one; missing manual coverage is not proof of universal absence. Do not transfer ECX335/343/350 bit depth, pinout or mode assumptions to ECX348.

### N2 — Establish reliable observability

Prefer an existing verified Pro access path. If a minimal diagnostic firmware change is required, use the XREAL example for architecture only and keep the vendor core. Validate target identity, full response shape, operation status, request association and complete probe success. The reviewed XREAL helper discards an inner status and its self-test can pass with missing replies; that behaviour is not acceptable evidence of a live Pro register read.

Keep the initial interface small and read-focused. Reject unknown registers and invalid arguments, and exclude OTP, analog overdrive, keys and arbitrary write endpoints. Setup writes required for reads must still be understood. A diagnostic firmware needs target-specific deployment/recovery qualification before hardware use.

**Output:** a justified access design and, only after the applicable separate approval, a known-state correlation. Returned data or an ACK alone is not enough.

### N3 — Correlate bridge receiving state with native panel operation

Identify the Pro bridge firmware's actual status interface and its STM32 consumer. The external LT7911 driver provides a hypothesis for an HDR-related event, not a portable register recipe. Record input transfer/signaling, internal format and the selected panel state separately.

**Output:** a genuine-HDR-input transition correlated with a native display mode, or a precise negative/inconclusive result. Receiver detection alone only establishes reception. A change in the wrong upstream condition invalidates an attempted fixed-input comparison.

### N4 — Minimal native-HDR prototype and validation

Only after N1 identifies a viable native mechanism, propose the smallest coordinated MCU/bridge/panel change that enables it. Keep HDR, refresh and IMU changes separate. Retain exact-stock hash checks, guarded patches, deterministic local output and a separately qualified updater/recovery path. A build that boots but merely alters an EDID flag is not completion.

The eventual test must establish genuine HDR input, the intended on-glasses response through both eyepieces and remaining precision/colour/thermal limits. No renderer target setting, smooth gradient, high brightness, mode label or status bit replaces that evidence. Native HDR and higher refresh are separate qualifications; neither 95 Hz nor the owner's approximate recollection is a ceiling.

## Deliverable boundary and remaining blockers

This pass completed document and pinned-source research, model/precision checks, PDF diagram inspection and same-author critique. It found real control and diagnostic pathways but no verified original-Pro native-PQ mode. No new firmware bytes, disassembly, patch build, upload, register trace or optical/refresh measurement was produced. The linked exact-panel manual remains unobtained; Pro artifact acquisition did not complete in the available runtime.

The source work does not require the owner to restate the goal, select another application or accept host mapping. Future implementation and results belong here; supporting research remains in bin. The next substantive decision follows an exact native-capability finding and a concrete intervention/recovery plan, not a speculative firmware-flashing attempt.
