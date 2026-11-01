# HDR hardware feasibility: what STM32 firmware would have to enable

Date: 2026-11-01. Status: source-backed engineering assessment, not an implemented or measured native-HDR unlock. Read with [the authoritative native-HDR requirement](NATIVE-HDR-REQUIREMENT-20261101.md). The target is original VITURE Pro hardware, with GlassVR retained. Genuine HDR input and on-glasses native response are required; SDR enhancement, host HDR-to-SDR output and a new STM32 software pixel mapper are not alternatives that satisfy this requirement.

## Decision

**Continue the exact-Pro panel/bridge capability investigation, but do not treat an HDR patch as implementation-ready.** Working HDR products combine adequate panels with a correct signal-processing/drive path. The closest example, RayNeo Air 4 Pro, has two identified PX8618 display processors in addition to the LT7911UXC receiver. The known Pro inventory does not identify that extra processing hardware. Therefore sharing OLED technology or a bridge family is insufficient to justify a firmware port.

A separate chip is not universally required: panel-integrated native PQ/transfer and colour resources could perform the essential functions. Pro 2's register tuning and original-Pro presets justify looking there. Their existence does not establish that the controls are capable of native PQ. The firmware-only route is conditional on locating that actual capability in the installed hardware.

## Evidence ownership

The [immutable bin snapshot 6884d0154f4515dfcfe38e4902b12c8cfcca7c23](https://github.com/Kyuugit/bin/tree/6884d0154f4515dfcfe38e4902b12c8cfcca7c23/viture-pro-xr-hdr-refresh-20261029) contains:

- [HDR enabling hardware and source evidence](https://github.com/Kyuugit/bin/blob/6884d0154f4515dfcfe38e4902b12c8cfcca7c23/viture-pro-xr-hdr-refresh-20261029/HDR-ENABLING-HARDWARE-20261101.md).
- [Same-author review and transferability checks](https://github.com/Kyuugit/bin/blob/6884d0154f4515dfcfe38e4902b12c8cfcca7c23/viture-pro-xr-hdr-refresh-20261029/HDR-ENABLING-HARDWARE-REVIEW-20261101.md).

The earlier [native-HDR investigation](NATIVE-HDR-INVESTIGATION-20261101.md), [firmware feasibility](FIRMWARE-FEASIBILITY-20261101.md) and [GlassVR correction](DECISION-GLASSVR-REFRESH-20261101.md) remain relevant. The new report adds actual successful-system architecture and Iris6 control-source evidence rather than replacing the accumulated research. Evidence remains in bin; implementation, experiments and decisions belong here.

## The key enabling elements

| Element | Function | Original-Pro status |
|---|---|---|
| HDR source/receiver path | Receive actual PQ content with correct primaries, range and numerical precision; do not silently transform it to SDR upstream | Family-level input capability documented. Exact fitted revision, active mode and emitted stream still require confirmation. |
| Native transfer response | Convert the HDR signal to the correct intended light response within the display range, whether integrated in panel electronics or another existing hardware block | **Unidentified decisive capability.** No documented native PQ setting or adequate exact-Pro transfer resource has been located. |
| Colour interpretation | Correctly handle the source colour space and the panel's actual primaries/calibration | White-balance controls and RGB/YCbCr conversion alone do not establish this. |
| Precision and final drive | Preserve needed distinctions through the relevant transforms and manage quantization/dither | Actual internal format and exact-panel drive precision remain unknown. Native HDR is not synonymous with a native ten-bit DAC. |
| Optical output | Produce useful highlight headroom, low black and colour volume through both lenses, consistently | Not measured for a native-HDR Pro mode. Panel-surface brightness is not eye-view luminance. |
| STM32 configuration | Select/init the native hardware state and coordinate both eyes and bridge | Plausible and supported by family examples; exact-Pro handler and transaction map still missing. |

## What the newly inspected Iris6 code changes

The RayNeo PX8618 marking now has a concrete family connection: Fairphone schematic text identifies it as Iris6. The pinned Fairphone-family Iris6 driver has actual branches separating HDR10/HLG from SDR enhancement, distinct LUT selection, MaxCLL updates, gamma and colour-management resources, dither tables, and firmware/calibration dependencies. These are reference examples of the missing functional questions, not just an advertised HDR flag.

The driver must not be copied into Pro as though it controls Lontium or Sony hardware. It programs a processor not identified in Pro. The exact RayNeo coefficients and active configuration were not decoded, and the same-chip comparison does not transfer phone calibration to near-eye displays. Apple's managed HDR display system likewise does not prove its bare panels accept raw PQ.

## Ordered implementation gates

| Gate | Concrete deliverable | Promotion / negative outcome |
|---|---|---|
| G1 — exact-Pro control semantics | Hash-identified preset/init handler map, actual target bus and register/table definitions | Native PQ selector or suitable native transfer/colour resources promote G2. Gain/offset/temperature-only controls reject that particular candidate, not all hardware possibilities. |
| G2 — essential-path sufficiency | Account for incoming PQ, internal precision, colour interpretation and output response; document what each installed block does | A complete plausible existing-hardware path justifies a minimal firmware design. A required but absent block makes it a hardware-redesign question, not a software-port task. |
| G3 — deployment qualification | Exact component/image format, integrity/authentication behaviour, permitted update regions and reachable recovery | A parser/checksum match is not enough. Retain separate offline builder and updater; no cross-flashing or protection/erase experiments are implied. |
| G4 — bounded native-HDR experiment | Genuine HDR test values, known input state, verified device setting and both-eye optical response within a declared range | Correct response localized to glasses supports native operation for those conditions. Host-converted input, unknown signaling or a badge-only result is inconclusive. Precision remains separately characterized. |
| G5 — practical release qualification | Wider content/peak conditions, declared clipping/roll-off, stable colour/brightness, reconnect and warm behaviour, GlassVR HDR-content compatibility | Keep native HDR, high-rate SBS and IMU changes independently qualified. Do not assume a successful low-rate HDR mode inherits the reported 95 Hz SDR configuration. |

The first native test need not recreate every Pixelworks feature. AI enhancement, HDR10+, motion interpolation and dynamic scene analysis are not prerequisites. A native PQ mode with correct colour/precision can be tested using content bounded by the usable display range. General content above that range requires an explicit handling policy. This avoids turning a large processor's optional features into unnecessary barriers while still requiring the essential HDR behaviour.

## Candidate choice and alternatives

First choice remains an existing panel-native PQ mode reachable through STM32. Second is a proven sufficient hardware-native transfer/colour facility already in the panel/bridge, configured by firmware rather than a software pixel mapper. Both need actual exact-Pro evidence; neither is established by a gamma slider.

XREAL's paired-firmware and readback methods are enabling tools for this investigation. Pro 2/Luma controls are discovery leads. Pixelworks/Iris6 is a functional reference and a demonstration of what added hardware can supply. Installing its software without equivalent silicon is not a third firmware-only route.

Adding an external or internal HDR processor would be a different hardware project with bus, power, heat, board and calibration requirements. It is not the requested unlock of the existing glasses and is not the default direction. No purchase or redesign has been initiated.

## Remaining blockers and completion boundary

The missing inputs are exact-Pro firmware/component mapping, panel suffix/programming definitions, an identified sufficient native transfer/colour mechanism, and device-specific deployment/recovery. Fresh original-Pro artifact acquisition failed again in the available runtime; historic hashes remain historical. Native HDR optical output and internal precision remain unmeasured.

This pass inspected documents and pinned source, including the new Iris6 branches, and recorded a same-author review. No original-Pro firmware was built or flashed, no live registers were read, no extra chip was added and no HDR/refresh measurement ran. The report also records failed schematic screenshot retrieval and denied direct Gerrit access rather than disguising those as completed checks.

The owner need not repeat the goal or reselect GlassVR. The next substantive conclusion must be a concrete exact-Pro hardware capability or a specific identified missing function, not another general claim that OLED supports HDR.
