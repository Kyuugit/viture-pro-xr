# Original VITURE Pro XR — native-HDR device extension

This repository owns decisions, future implementation and experiments for the **original VITURE Pro XR**. Supporting research stays in [the existing bin archive](https://github.com/Kyuugit/bin/tree/main/viture-pro-xr-hdr-refresh-20261029). GlassVR remains the integration target. Pro 2, Luma, XREAL and RayNeo are mechanism references, not cross-flash targets.

## Current conclusion — 1 November 2026

**Start with [HDR hardware feasibility and implementation gates](HDR-HARDWARE-FEASIBILITY-20261101.md).** A usable HDR system needs both an adequate panel and correct signal-to-light processing/drive. The closest successful glasses comparison, RayNeo Air 4 Pro, contains two teardown-identified PX8618 processors as well as LT7911UXC. Newly inspected Iris6-family source exposes separate HDR-input and SDR-enhancement modes, LUT selection, content-light control, colour/gamma resources and calibration dependencies.

That explains a real hardware pathway; it is not a Pro firmware port. The known Pro inventory does not identify that added processor. Firmware-only native HDR depends on finding equivalent essential capabilities in the installed bridge or panel electronics. A separate processor is not universally required, but neither OLED technology, HDR reception nor gamma presets alone proves the necessary path exists.

The [hardware research](https://github.com/Kyuugit/bin/blob/6884d0154f4515dfcfe38e4902b12c8cfcca7c23/viture-pro-xr-hdr-refresh-20261029/HDR-ENABLING-HARDWARE-20261101.md) and [same-author review](https://github.com/Kyuugit/bin/blob/6884d0154f4515dfcfe38e4902b12c8cfcca7c23/viture-pro-xr-hdr-refresh-20261029/HDR-ENABLING-HARDWARE-REVIEW-20261101.md) retain source pins, confidence, exact-model limits and failed access checks. Native HDR and native ten-bit panel DACs remain separate claims; correctly applied dithering is not SDR enhancement.

## Authoritative requirement

[Native-HDR requirement](NATIVE-HDR-REQUIREMENT-20261101.md): genuine HDR input displayed by the glasses' existing hardware, enabled through STM32 and, where required, bridge/panel configuration or firmware. SDR enhancement, host HDR-to-SDR output and a new MCU software pixel mapper do not satisfy the objective. STM32 is the control entry point; it need not process every video pixel.

The earlier MCU cycles-per-pixel argument addressed a different architecture. Host patterns are diagnostics, not replacement outcomes. Keep the [GlassVR high-refresh correction](DECISION-GLASSVR-REFRESH-20261101.md) in force: use the author's existing original-Pro configuration as the refresh starting point. Neither 95 Hz nor the owner's approximate recollection is a ceiling, and a successful SDR mode does not prove HDR at the same rate.

## Current ordered work

| Gate | Required output |
|---|---|
| Exact-Pro controls | Hash-identified stock preset/init functions, target buses and register/table semantics. Pro 2/Luma/XREAL findings help locate them, not assume their capabilities. |
| Essential native-HDR capability | A native PQ mode or sufficient existing transfer/colour hardware, with correct precision and ordering. Limited gain, offset or fixed SDR gamma alone is insufficient. |
| Deployment | Pro-specific image/component validation, authentication/update behaviour and reachable recovery. Offline builder and hardware updater remain separate. |
| Bounded native-HDR test | Known genuine HDR input and through-eyepiece response from both eyes, localized to the glasses. A badge, ACK, EDID or boot success is insufficient. |
| Practical qualification | Colour/headroom, declared clipping or roll-off, stability, reconnect/warm behaviour and GlassVR HDR-source compatibility. Qualify refresh and IMU changes independently. |

A native panel PQ mode could avoid a separate HDR chip; AI enhancement, dynamic scene analysis and HDR10+ are not prerequisites for a bounded native-HDR experiment. Conversely, a software port of Pixelworks controls without matching silicon cannot supply its hardware functions. Adding a processor would be a different hardware project, not the default firmware-only goal.

## Evidence and previous decisions

[Current hardware decision](HDR-HARDWARE-FEASIBILITY-20261101.md) extends [native-HDR investigation](NATIVE-HDR-INVESTIGATION-20261101.md), [firmware feasibility](FIRMWARE-FEASIBILITY-20261101.md) and [device-first decision](DECISION-DEVICE-FIRST-20261101.md). Original-Pro stock presets and Pro 2 panel-register tuning remain the strongest exact/family access leads. The XREAL diagnostic-validation corrections remain applicable. The Pro/XREAL container relationship is still an untested hypothesis.

The [original decision](DECISION-20261101.md) and [original handoff](HANDOFF.md) retain historical tools and requirements, not a current host-first priority. The [preceding complete index](https://github.com/Kyuugit/viture-pro-xr/blob/4871a2a402bb53165b2c16b799948c5e7c8cf4d2/README.md) preserves earlier navigation. Supporting technical reports and evidence history remain in bin rather than being duplicated here.

## Completion boundary

This is a researched conditional implementation direction, not a shipped native-HDR firmware. The latest pass completed source/document comparison and same-author review; it did not build/flash a Pro image, read live registers, validate the container hypothesis or perform optical, IMU or refresh measurements. Failed original-Pro artifact retrieval and schematic screenshot attempts are explicitly recorded, not treated as device limitations.

The next decisive result is an exact-Pro native hardware capability or an identified missing essential function. Source research does not authorize installation, device writes, flashing, purchases or outreach. Keep proprietary payloads and private device data out of public releases; distinguish proposed, built, accepted and measured results.
