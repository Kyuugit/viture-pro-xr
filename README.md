# Original VITURE Pro XR — device-side extension

This repository owns decisions, future implementation and experiments for the **original VITURE Pro XR**. Supporting research stays in [the existing bin archive](https://github.com/Kyuugit/bin/tree/main/viture-pro-xr-hdr-refresh-20261029). Original Pro is not Pro 2, Luma or Beast; related devices provide mechanisms to investigate, not firmware to cross-flash.

## Current native-HDR investigation — 1 November 2026

**Start with [Native-HDR investigation: concrete pathways and next work](NATIVE-HDR-INVESTIGATION-20261101.md).** The strongest new lead is VITURE's explicit description of Pro 2 panel-register gamma tuning, combined with original-Pro stock colour presets. Trace the original Pro's preset/panel initialization to actual hardware controls before proposing an HDR patch. Luma Pro supplies a further control-family comparison; the XREAL kit supplies implemented MCU diagnostic and coordinated bridge/panel patterns.

The [pathway evidence](https://github.com/Kyuugit/bin/blob/478f406996d07701e07b2c6456997243c9d33eb4/viture-pro-xr-hdr-refresh-20261029/NATIVE-HDR-PATHWAYS-20261101.md) also follows a neighbouring Sony panel's native gamma/precision diagram and an LT7911UXC-family HDR-related status implementation. **These establish concrete investigative pathways, not a verified native PQ mode on original Pro.** The [source review](https://github.com/Kyuugit/bin/blob/478f406996d07701e07b2c6456997243c9d33eb4/viture-pro-xr-hdr-refresh-20261029/NATIVE-HDR-PATHWAYS-REVIEW-20261101.md) records diagnostic-validation gaps that must not be copied into a Pro port.

## Authoritative requirement

[Native-HDR requirement](NATIVE-HDR-REQUIREMENT-20261101.md): genuine HDR input displayed by the glasses' native hardware, enabled/configured through the STM32 and, where required, bridge/panel firmware. SDR-to-HDR enhancement, host HDR-to-SDR output and a new MCU software pixel mapper do not satisfy the goal. The STM32 is the control entry point; the video stream need not be processed by its CPU.

The historical MCU cycles-per-pixel calculation does not argue against enabling a native hardware mode. Host patterns may serve as diagnostic references; they do not replace the objective. Keep **GlassVR** as the integration target and its already-reported high-rate SBS path as the refresh starting point.

## Current priorities

| Workstream | Next substantive output |
|---|---|
| Original-Pro native display controls | Exact-artifact preset/init handler map, target bus and register semantics; distinguish gain/temperature-only changes from native transfer capabilities. |
| Exact-panel capability | Fitted suffix, programming evidence, native PQ/transfer operating conditions and internal precision. Do not substitute another Sony panel's specifications. |
| Diagnostic access | Existing verified access first; otherwise a minimal Pro-specific firmware design with complete status/response validation and qualified recovery. |
| Receiver/native-mode coordination | Correlate genuine HDR input, Pro-specific bridge status and a real native display mode. A status name is not an enable bit. |
| Firmware deployment | Guarded local builder retaining the vendor core; separate component-aware updater and target-specific recovery. The prior Pro/XREAL container hypothesis remains untested. |
| Full-SBS refresh | Reuse and refine GlassVR's CRU/SBS/connection/firmware route, qualifying distinct frames in both eyes. Neither 95 Hz nor the owner's recollection is a ceiling. |
| IMU resource use | Measure the provider-lifetime/shared-resource question independently; no contention result has been established. |

## Evidence and previous decisions

The [current investigation](NATIVE-HDR-INVESTIGATION-20261101.md) links the immutable research snapshot and gives ordered source/implementation work. Its control-path priority extends [firmware feasibility](FIRMWARE-FEASIBILITY-20261101.md), subject to the native-HDR requirement. The [device-first decision](DECISION-DEVICE-FIRST-20261101.md) and [GlassVR refresh correction](DECISION-GLASSVR-REFRESH-20261101.md) remain in force.

The [original consolidated decision](DECISION-20261101.md) and [initial handoff](HANDOFF.md) retain historical tools and validation requirements, but their host-first priorities are superseded. The [preceding project index](https://github.com/Kyuugit/viture-pro-xr/blob/25fd89628f397785123075a580bb0d77c486454f/README.md) preserves the previous navigation. Earlier evidence and corrections were not silently rewritten.

## Completion boundary

This is source research, not a shipped firmware or native-HDR demonstration. The new pass inspected manufacturer documents, pinned implementations and PDF diagrams and performed same-author critique. No fresh original-Pro firmware acquisition, binary disassembly, checksum validation, patch build, upload, register capture, optical result, IMU benchmark or refresh qualification occurred. Historical hashes, calculations and other authors' tests retain their original scope.

The exact original-Pro component/control map and panel programming evidence are the decisive missing inputs. Firmware acceptance, control reachability and native HDR capability remain separate gates. Any future result must identify model/build, requested versus actual signal, device state, optical uncertainty and negative/inconclusive outcomes. Evidence remains in bin; future implementation and results belong here. No hardware action, installation, purchase or outreach is authorized merely by a source finding.
