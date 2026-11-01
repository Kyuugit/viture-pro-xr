# Requirement correction: native HDR enabled through STM32 firmware

Date: 2026-11-01. This records the owner's clarification: the objective is to use the original Pro panel with true native HDR through the STM32-controlled device configuration, not introduce software that converts SDR into an HDR-looking image. This clarification takes precedence over broader fallback or software-conversion suggestions in earlier decisions. It is a scope correction, not a newly demonstrated hardware capability.

## Required outcome

Enable genuine HDR-source presentation by the original VITURE Pro's own display hardware, through an understood change to its STM32 firmware and, if required, its bridge configuration or firmware. Keep GlassVR as the integration target. The source for the native-HDR investigation is actual HDR content or controlled HDR test values, initially HDR10/PQ—not an SDR source enhanced after the fact.

The STM32 is the intended firmware/control entry point. Investigate what it can enable, select or configure in the installed video bridge and panel electronics. Do not assume the full video pixel stream must traverse the STM32 CPU, or that the requested solution requires a new CPU-per-pixel conversion algorithm.

## Correction to the previous explanation

The previous response spent time ruling out MCU-per-pixel video processing and discussing replacement mappings. That addressed a mechanism the owner was not proposing. The recorded cycles-per-pixel arithmetic is not a feasibility argument against STM32 firmware enabling an existing hardware-native HDR path. Retain the arithmetic as historical evidence about a different hypothetical architecture, not as a gate on this requirement.

SDR-to-HDR enhancement, host HDR-to-SDR presentation, raised brightness, and an HDR EDID declaration alone are not substitutes for the required native result. A useful RGB or refresh improvement remains a separate deliverable; it does not satisfy the native-HDR requirement.

Decoding an actual PQ-encoded HDR source with an existing hardware transfer function is different from synthesizing HDR from SDR. Configuring such an existing function from STM32 firmware is in scope. A proposal to emulate the result through a new host shader or MCU software pixel mapper is not the requested direction. Panel-native precision must still be reported separately; this clarification does not establish either 8-bit or 10-bit panel operation.

## What the hardware evidence supports

The [LT7911UXC U2 R1.0 manufacturer brief](https://www.lontiumsemi.com/UploadFiles/2022-03/LT7911UXC_U2_Brief_R1.0.pdf), pages 1–2, was rechecked as text and screenshots. It describes a DP-to-MIPI/LVDS video path, static HDR10 receiver support, an embedded processor/firmware, and an external I2C configuration interface. Those are relevant to control-driven enablement. It is not a full register manual and does not establish an original-Pro native HDR mode or the STM32's actual board-level control transactions.

The working distinction is a video path through the bridge to the panels, and a control path by which firmware selects/configures device operation. This is an architectural investigation target, not a newly traced Pro schematic. Exact STM32-to-bridge/panel connections and reachable operations remain to be mapped.

The existing [chipset/panel evidence](https://github.com/Kyuugit/bin/blob/ffcb915eb988b52b3d5131d04a77473445a15ff0/viture-pro-xr-hdr-refresh-20261029/CHIPSET-PANEL-HDR-20261101.md) preserves the unresolved exact-panel programming and precision questions. Neither the missing manual nor the receiver feature list justifies assuming that an enableable native HDR mode exists or does not exist.

## Focus of the next investigation

1. Trace the original-Pro STM32 firmware's display initialization, mode selection and bridge/panel configuration. Locate concrete register transactions, table selection and any HDR-dependent branch; do not invent an HDR-enable bit from neighbouring-chip examples.
2. Establish what the exact fitted bridge revision and panel suffix support: native transfer modes, internal output format, precision and associated mode requirements. Correlate those controls with the STM32 path rather than substitute a new software mapping design.
3. Determine what changes are required to advertise, receive and correctly display a genuine HDR input. These may be coordinated settings, not necessarily an STM32-only patch. Keep signal acceptance, hardware response and native panel precision separate.
4. Qualify a candidate with known HDR input and through-eyepiece output evidence, while establishing that the host is not secretly substituting an SDR mapping. A UI toggle, successful command or firmware boot is not a native-HDR result.

The XREAL paired-firmware work remains a reference for modifying device configuration; Pro 2 work remains a protocol-discovery reference. Neither proves the Pro's native HDR capability. GlassVR's reported high-rate SBS setup remains the refresh starting point, without making 95 Hz a ceiling.

## Decision boundary

The question is now explicitly: **Can original-Pro STM32 firmware enable/configure a real native HDR display path already supported by the installed bridge and panel hardware?** If evidence shows that path requires another on-device component's configuration or firmware, record that dependency. If an essential hardware feature is absent, report the specific missing function rather than silently replacing the objective with SDR conversion.

No new firmware bytes, patch, device test, optical result or permission to flash follows from this correction. Future implementation and decisions remain in this repository; supporting source evidence and its history remain in the existing bin folder.
