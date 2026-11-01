# Original VITURE Pro XR — native-HDR device extension

This repository owns decisions, future implementation and experiments for the **original VITURE Pro XR**. Supporting research stays in [the existing bin archive](https://github.com/Kyuugit/bin/tree/main/viture-pro-xr-hdr-refresh-20261029). GlassVR remains the integration target. Pro 2, Luma, XREAL and RayNeo are mechanism references, not cross-flash targets.

## Current correction — do not assume a built-in PQ/HDR mode

**There is no established selectable PQ/HDR mode on the original Pro in the specifications, advertising, register documentation or implementation examined. The recommendation to select one was unsupported and is withdrawn.** Read the correction in [HDR hardware feasibility](HDR-HARDWARE-FEASIBILITY-20261101.md) before earlier recommendations. This takes precedence over hypothetical native-mode selection in previous project documents and immutable research snapshots; the historical evidence is preserved, not endorsed as proof of a built-in feature.

The actual engineering question is whether the installed hardware's documented or reverse-engineered programmable functions are sufficient to implement genuine HDR through device firmware. Identify those functions, their limits and their place in the signal path first. Do not presume a hidden switch, arbitrary gamma LUT, PQ preset or unadvertised HDR engine. No sufficient original-Pro implementation has yet been established.

## Current hardware evidence — 1 November 2026

A usable HDR system needs both an adequate panel and correct signal-to-light processing/drive. The closest successful glasses comparison, RayNeo Air 4 Pro, contains two teardown-identified PX8618 processors as well as LT7911UXC. Inspected Iris6-family source exposes separate HDR-input and SDR-enhancement modes, LUT selection, content-light control, colour/gamma resources and calibration dependencies.

That explains a real hardware pathway; it is not a Pro firmware port. The known Pro inventory does not identify that added processor. A firmware-only implementation must account for every essential function using hardware actually present. OLED technology, HDR reception and gamma presets alone do not establish sufficiency.

The [hardware research](https://github.com/Kyuugit/bin/blob/6884d0154f4515dfcfe38e4902b12c8cfcca7c23/viture-pro-xr-hdr-refresh-20261029/HDR-ENABLING-HARDWARE-20261101.md) and [same-author review](https://github.com/Kyuugit/bin/blob/6884d0154f4515dfcfe38e4902b12c8cfcca7c23/viture-pro-xr-hdr-refresh-20261029/HDR-ENABLING-HARDWARE-REVIEW-20261101.md) retain source pins, confidence, exact-model limits and failed access checks. Their speculative selectable-mode recommendations are superseded by the correction above. Native HDR and native ten-bit panel DACs remain separate claims; correctly applied dithering is not SDR enhancement.

## Authoritative requirement

[Native-HDR requirement](NATIVE-HDR-REQUIREMENT-20261101.md): genuine HDR input displayed by the glasses' existing hardware, implemented/configured through STM32 and, where required, bridge/panel firmware. The requirement describes the desired outcome, not an existing feature waiting to be selected. SDR enhancement, host HDR-to-SDR output and a new MCU software pixel mapper do not satisfy the objective. STM32 is the control entry point; it need not process every video pixel.

The earlier MCU cycles-per-pixel argument addressed a different architecture. Host patterns are diagnostics, not replacement outcomes. Keep the [GlassVR high-refresh correction](DECISION-GLASSVR-REFRESH-20261101.md) in force: use the author's existing original-Pro configuration as the refresh starting point. Neither 95 Hz nor the owner's approximate recollection is a ceiling, and a successful SDR mode does not prove HDR at the same rate.

## Current ordered work

| Gate | Required output |
|---|---|
| Exact-Pro controls | Hash-identified stock preset/init functions, target buses and register/table semantics, permitted ranges and precision. Pro 2/Luma/XREAL findings help locate them, not assume their capabilities. |
| Essential-function sufficiency | Demonstrate whether the identified programmable hardware can implement the required response and colour handling with correct precision and ordering. No presumed PQ selector or arbitrary LUT. Limited gain, offset or fixed SDR gamma must not be relabelled an HDR engine. |
| Deployment | Pro-specific image/component validation, authentication/update behaviour and reachable recovery. Offline builder and hardware updater remain separate. |
| Bounded native-HDR test | Known genuine HDR input and through-eyepiece response from both eyes, localized to the glasses. A badge, ACK, EDID or boot success is insufficient. |
| Practical qualification | Colour/headroom, declared clipping or roll-off, stability, reconnect/warm behaviour and GlassVR HDR-source compatibility. Qualify refresh and IMU changes independently. |

There is currently an investigation to perform, not a qualified native-HDR implementation candidate. A software port of Pixelworks controls without matching silicon cannot supply its hardware functions. Adding a processor would be a different hardware project, not the default firmware-only goal.

## Evidence and previous decisions

[Current hardware decision](HDR-HARDWARE-FEASIBILITY-20261101.md) corrects and extends [native-HDR investigation](NATIVE-HDR-INVESTIGATION-20261101.md), [firmware feasibility](FIRMWARE-FEASIBILITY-20261101.md) and [device-first decision](DECISION-DEVICE-FIRST-20261101.md). Original-Pro stock presets and Pro 2 panel-register tuning remain access/control leads, not HDR-feature evidence. The XREAL diagnostic-validation corrections remain applicable. The Pro/XREAL container relationship is still an untested hypothesis.

The [original decision](DECISION-20261101.md) and [original handoff](HANDOFF.md) retain historical tools and requirements, not a current host-first priority. The [index before this correction](https://github.com/Kyuugit/viture-pro-xr/blob/0db68c30ef88622a4b03502a8309a4d92d1e7022/README.md) preserves the earlier wording. Supporting technical reports and evidence history remain in bin rather than being duplicated here.

## Completion boundary

This is a researched conditional implementation direction, not a shipped native-HDR firmware. The preceding pass completed source/document comparison and same-author review; it did not build/flash a Pro image, read live registers, validate the container hypothesis or perform optical, IMU or refresh measurements. Failed original-Pro artifact retrieval and schematic screenshot attempts are explicitly recorded, not treated as device limitations. The present correction withdraws an unsupported recommendation and introduces no new hardware evidence.

The next decisive result must identify actual original-Pro functions and their sufficiency or a specific missing essential function. Source research does not authorize installation, device writes, flashing, purchases or outreach. Keep proprietary payloads and private device data out of public releases; distinguish proposed, built, accepted and measured results.
