# HDR hardware feasibility: what STM32 firmware would have to implement or configure

Date: 2026-11-01. Status: source-backed engineering assessment, not an implemented or measured native-HDR result. Read with [the authoritative native-HDR requirement](NATIVE-HDR-REQUIREMENT-20261101.md). The target is original VITURE Pro hardware, with GlassVR retained. Genuine HDR input and on-glasses native response are required; SDR enhancement, host HDR-to-SDR output and a new STM32 software pixel mapper are not alternatives that satisfy this requirement.

## Correction — no evidenced built-in PQ/HDR mode

The owner correctly challenged the repeated recommendation to select an existing panel-native PQ/HDR mode. **No such mode has been established in the original Pro's specifications, advertising, register documentation or inspected implementation. Recommending it as the first-choice route was unsupported and is withdrawn.** This correction takes precedence over selectable-mode suggestions in earlier project documents and linked research snapshots; those remain historical records, not current recommendations.

Do not substitute an imagined hidden switch, undocumented HDR preset or presumed arbitrary LUT for missing evidence. The research question is whether the installed hardware's actually documented or reverse-engineered programmable functions are sufficient to implement the required HDR behaviour through device firmware. Those functions, their capacity and their location must be established before proposing an implementation. No adequate original-Pro transfer/colour facility has yet been identified. This correction reports no new hardware finding.

## Decision

**Continue the exact-Pro panel/bridge capability investigation, but do not treat an HDR patch as implementation-ready.** Working HDR products combine adequate panels with a correct signal-processing/drive path. The closest example, RayNeo Air 4 Pro, has two identified PX8618 display processors in addition to the LT7911UXC receiver. The known Pro inventory does not identify that extra processing hardware. Therefore sharing OLED technology or a bridge family is insufficient to justify a firmware port.

Pro 2's register tuning and original-Pro presets justify identifying the actual controls, not assuming HDR support. Classify the controls and establish their limits before evaluating whether firmware can configure them to implement native HDR. A separate processor is not assumed mandatory, but an equivalent sufficient function in the existing hardware must be demonstrated rather than invented.

## Evidence ownership

The [immutable bin snapshot 6884d0154f4515dfcfe38e4902b12c8cfcca7c23](https://github.com/Kyuugit/bin/tree/6884d0154f4515dfcfe38e4902b12c8cfcca7c23/viture-pro-xr-hdr-refresh-20261029) contains:

- [HDR enabling hardware and source evidence](https://github.com/Kyuugit/bin/blob/6884d0154f4515dfcfe38e4902b12c8cfcca7c23/viture-pro-xr-hdr-refresh-20261029/HDR-ENABLING-HARDWARE-20261101.md).
- [Same-author review and transferability checks](https://github.com/Kyuugit/bin/blob/6884d0154f4515dfcfe38e4902b12c8cfcca7c23/viture-pro-xr-hdr-refresh-20261029/HDR-ENABLING-HARDWARE-REVIEW-20261101.md).

The earlier [native-HDR investigation](NATIVE-HDR-INVESTIGATION-20261101.md), [firmware feasibility](FIRMWARE-FEASIBILITY-20261101.md) and [GlassVR correction](DECISION-GLASSVR-REFRESH-20261101.md) retain useful evidence, subject to the correction above. The hardware report adds successful-system architecture and Iris6 control-source evidence. Its speculative selectable-mode recommendations are superseded, not new evidence for an original-Pro feature. Evidence remains in bin; implementation, experiments and decisions belong here.

## The key enabling elements

| Element | Function | Original-Pro status |
|---|---|---|
| HDR source/receiver path | Receive actual PQ content with correct primaries, range and numerical precision; do not silently transform it to SDR upstream | Family-level input capability documented. Exact fitted revision, active mode and emitted stream still require confirmation. |
| Native transfer response | Produce the correct intended light response from genuine HDR input within the display range | **Unidentified decisive capability.** No sufficient exact-Pro programmable resource or implementation has been established. Do not assume a selectable HDR mode. |
| Colour interpretation | Correctly handle the source colour space and the panel's actual primaries/calibration | White-balance controls and RGB/YCbCr conversion alone do not establish this. |
| Precision and final drive | Preserve needed distinctions through the relevant transforms and manage quantization/dither | Actual internal format and exact-panel drive precision remain unknown. Native HDR is not synonymous with a native ten-bit DAC. |
| Optical output | Produce useful highlight headroom, low black and colour volume through both lenses, consistently | Not measured for native HDR on Pro. Panel-surface brightness is not eye-view luminance. |
| STM32 configuration | Configure identified hardware resources and coordinate both eyes and bridge | Family examples motivate tracing; exact-Pro handler and transaction map still missing. Control access alone does not establish HDR capability. |

## What the inspected Iris6 code changes

The RayNeo PX8618 marking has a concrete family connection: Fairphone schematic text identifies it as Iris6. The pinned Fairphone-family Iris6 driver has actual branches separating HDR10/HLG from SDR enhancement, distinct LUT selection, MaxCLL updates, gamma and colour-management resources, dither tables, and firmware/calibration dependencies. These are reference examples of functional requirements, not just an advertised HDR flag.

The driver must not be copied into Pro as though it controls Lontium or Sony hardware. It programs a processor not identified in Pro. The exact RayNeo coefficients and active configuration were not decoded, and the same-chip comparison does not transfer phone calibration to near-eye displays. Apple's managed HDR display system likewise does not prove its bare panels accept raw PQ.

## Ordered implementation gates

| Gate | Concrete deliverable | Promotion / negative outcome |
|---|---|---|
| G1 — exact-Pro control semantics | Hash-identified preset/init handler map, actual target bus and register/table definitions, including permitted ranges and precision | Establish the actual programmable functions before judging HDR feasibility. Gain/offset/temperature-only findings must not be relabelled an HDR engine. No presumed PQ selector. |
| G2 — essential-path sufficiency | Account for incoming PQ, internal precision, colour interpretation and output response; document what each installed block can implement | A sufficient existing-hardware design justifies a minimal firmware proposal. Unknown functions remain unknown. A required but demonstrated absent function makes it a hardware-redesign question, not a software-port task. |
| G3 — deployment qualification | Exact component/image format, integrity/authentication behaviour, permitted update regions and reachable recovery | A parser/checksum match is not enough. Retain separate offline builder and updater; no cross-flashing or protection/erase experiments are implied. |
| G4 — bounded native-HDR experiment | Genuine HDR test values, known input state, a justified device configuration and both-eye optical response within a declared range | Correct response localized to glasses supports native operation for those conditions. Host-converted input, unknown signaling or a badge-only result is inconclusive. Precision remains separately characterized. |
| G5 — practical release qualification | Wider content/peak conditions, declared clipping/roll-off, stable colour/brightness, reconnect and warm behaviour, GlassVR HDR-content compatibility | Keep native HDR, high-rate SBS and IMU changes independently qualified. Do not assume a successful low-rate HDR implementation inherits the reported 95 Hz SDR configuration. |

A future implementation test need not recreate every Pixelworks feature. AI enhancement, HDR10+, motion interpolation and dynamic scene analysis are not prerequisites. Once a sufficient actual hardware implementation is established, it can initially be tested with genuine HDR content bounded by the usable display range and with correct colour/precision. General content above that range requires an explicit handling policy. This is a test-design distinction, not evidence of an existing HDR mode.

## Candidate choice and alternatives

**No original-Pro native-HDR implementation candidate is yet qualified.** The next research candidate is exact-Pro control/function mapping, followed by a sufficiency assessment of the discovered resources. Do not rank selecting a built-in PQ/HDR mode as an available route, and do not assume programmable gamma means an arbitrary transfer table. Any firmware design must name actual functions and explain how their documented or reverse-engineered capabilities meet the required native HDR behaviour.

XREAL's paired-firmware and readback methods are enabling tools for this investigation. Pro 2/Luma controls are discovery leads. Pixelworks/Iris6 is a functional reference and a demonstration of what added hardware can supply. Installing its software without equivalent silicon is not a firmware-only route.

Adding an external or internal HDR processor would be a different hardware project with bus, power, heat, board and calibration requirements. It is not the requested extension of the existing glasses and is not the default direction. No purchase or redesign has been initiated.

## Remaining blockers and completion boundary

The missing inputs are exact-Pro firmware/component mapping, panel suffix/programming definitions, an identified sufficient native transfer/colour mechanism, and device-specific deployment/recovery. Fresh original-Pro artifact acquisition failed in the preceding research runtime; historic hashes remain historical. Native HDR optical output and internal precision remain unmeasured.

The preceding pass inspected documents and pinned source, including the Iris6 branches, and recorded a same-author review. No original-Pro firmware was built or flashed, no live registers were read, no extra chip was added and no HDR/refresh measurement ran. It also recorded failed schematic screenshot retrieval and denied direct Gerrit access rather than disguising those as completed checks. This correction changes the recommendation, not the empirical evidence.

The owner need not repeat the goal or reselect GlassVR. The next substantive conclusion must identify actual original-Pro programmable functions and their sufficiency or a specific missing function—not repeat a hypothetical built-in feature or another general claim that OLED supports HDR.
