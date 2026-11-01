# Firmware-extension feasibility and next implementation direction

Date: 2026-11-01. Status: **source-supported development proposal, not a built or flashable original-Pro firmware release**. This extends [the device-first decision](DECISION-DEVICE-FIRST-20261101.md), not the superseded host-first recommendation. GlassVR remains the target, and [its reported high-rate setup](DECISION-GLASSVR-REFRESH-20261101.md) remains the refresh starting point. The owner's device-side preference is settled.

## Decision

Develop toward **a Pro-specific guarded patch/build system that retains the vendor firmware core**, using the XREAL kit as the firmware-engineering reference and the Pro 2 project as a protocol-discovery reference. Do not treat either project's binaries or updater as compatible with original Pro. A complete replacement firmware is a fallback engineering strategy, not the first deliverable.

There are two independent feasibility gates:

1. **Firmware deployment:** understand the original-Pro artifact/component format, validation, target selection, update state machine and recovery well enough to install a specific modification.
2. **Feature implementation:** identify actual hardware that can perform the desired operation. Firmware acceptance alone cannot create a missing video-processing block.

For native HDR, gate 2 is the important unresolved architectural question. HDR-capable reception is documented for the bridge family, and micro-OLED technology is capable of HDR display systems. What is not yet established is the original Pro's reachable PQ-to-panel transformation and its internal precision. No source found justifies promising an HDR unlock; none establishes a blanket micro-OLED or receiver-level impossibility.

## Supporting evidence — retained in bin

The immutable [research snapshot ffcb915eb988b52b3d5131d04a77473445a15ff0](https://github.com/Kyuugit/bin/tree/ffcb915eb988b52b3d5131d04a77473445a15ff0/viture-pro-xr-hdr-refresh-20261029) contains:

- [Firmware portability, container hypothesis and shipping contract](https://github.com/Kyuugit/bin/blob/ffcb915eb988b52b3d5131d04a77473445a15ff0/viture-pro-xr-hdr-refresh-20261029/FIRMWARE-PORTABILITY-20261101.md).
- [Chipset/panel HDR evidence, comparisons, candidates and review](https://github.com/Kyuugit/bin/blob/ffcb915eb988b52b3d5131d04a77473445a15ff0/viture-pro-xr-hdr-refresh-20261029/CHIPSET-PANEL-HDR-20261101.md).
- [Executed arithmetic record](https://github.com/Kyuugit/bin/blob/ffcb915eb988b52b3d5131d04a77473445a15ff0/viture-pro-xr-hdr-refresh-20261029/MCU-VIDEO-ARITHMETIC-20261101.json), explicitly not a device test.

These supplement, rather than replace, the historical firmware hashes, independent reviews, GlassVR correction and device-first evidence. Future implementation, experiment results and decisions belong in this repository.

## What can be reused

| Reference | Reuse | Do not infer |
|---|---|---|
| Pro 2 runtime work | Official SDK logging correlated with USB traces; independent codec; strict model dispatch; labelled handler discovery | A documented flasher, original-Pro protocol compatibility, or an unsigned boot policy. Runtime and update protocols are separate. |
| XREAL Air-family kit | Exact-input hashes, guarded local patches, component-aware verification, deterministic output, paired MCU/bridge reasoning, recovery qualification | That changing VID/PID makes its updater safe for Pro; that its fallback exists on Pro; that its panel settings or authentication behavior transfer. |
| Original-Pro GlassVR report | Existing full-SBS operational configuration and a concrete firmware-version dependency to investigate | A 95 Hz ceiling, proof of automatic firmware patching, or a measured HDR path. |

The newly promising format lead is that XREAL Air's documented 24-byte MCU header resembles the historical Pro artifact: length-minus-eight at offset 4, identity field beginning at offset 8, and plausible vector data beginning at 0x18. The exact checksum hypothesis is recorded in bin. **It has not been verified on Pro bytes.** A checksum match would help build a parser; it would not prove that modified images boot or that firmware is unsigned.

## Hardware interpretation

The original-Pro bridge family explicitly lists static HDR10 reception and higher-depth input. The inspected brief does not identify a programmable PQ EOTF, tone mapper or pixel LUT. Neighbouring Lontium chips demonstrate both broader output capabilities and mode-dependent precision restrictions; their extra features cannot be imported into the fitted chip by installing their firmware.

Sony's exact ECX348E panel family is identified by the teardown, but the full exact-suffix programming manual remains missing. An advertised ECX348ENA-6 datasheet is an acquisition lead, not obtained evidence. The Sony ECX343E example's 8-bit DAC does not settle ECX348E precision. Newer ECX350F brightness and larger ECX344A gamut show separate dimensions of progress, not drop-in replacements or proof of a PQ mode in Pro.

A useful native HDR system need not have a panel that parses metadata itself. The bridge or a configurable panel transfer stage can perform the conversion. Finding such a reachable stage is the preferred route. A simple gamma exponent, brightness increase, RGB↔YCbCr block or HDR EDID declaration is not that evidence.

## Next work packages and decision outcomes

| ID / priority | Work | Concrete completion / branching condition |
|---|---|---|
| F0 — offline, first | Obtain authorized Pro artifact copies, confirm hashes and test the recorded container hypothesis | Bounded parser output and checksum/address-map evidence. A mismatch is preserved, then checked against actual updater logic. Do not alter the file to make it fit. |
| F1 — source, parallel | Map MCU, bridge code/data, panel setup and update relationships; recover the GlassVR-relevant same-selector version pair | Traceable component/handler map and actual mode/profile differences. N6P/N6PL variants are not a release pair. Missing component bytes remain a gap. |
| H0 — source, parallel | Identify exact panel suffix/manual and reachable transfer/gamma/LUT/colour controls | Describe the actual per-pixel stage, its range, precision and ordering. If none is found, do not claim absence solely from brief documentation. Seek the missing register or implementation evidence. |
| F2 — offline prototype | Implement a minimal builder for one understood Pro-specific change | Reject unknown input hashes; check original bytes; preserve unrelated data; deterministic output and independent validation. This produces an experimental artifact, not permission to deploy. |
| F3 — deployment gate | Establish official update state machine, image authentication and target-specific restore/recovery | Evidence that the intended regions and components can be restored, including a reachable recovery mode. A stock image alone is insufficient. A separate approved test is required. |
| H1 — native-PQ gate | At a known-good mode, compare controlled encoded input and signaling with through-eyepiece response | Localize an intended repeatable transformation to the glasses; record upstream uncertainty. Optical precision is a separate claim. Unverified signaling yields inconclusive, not failure. |
| R1 — retained refresh work | Reproduce/refine the GlassVR high-rate path and any specific firmware change | Full transmitted 3840×1080, correct eye split and distinct frames in both eyes over stated conditions. Do not replace this with OS-only Hz. |

A small validated RGB-path or mode-selection extension can be the first meaningful release even if native PQ remains blocked. Do not entangle a refresh patch, an HDR curve, IMU changes and firmware-version changes into one experiment.

## Proposed distribution design

Publish the builder/patch logic, compatibility manifest, source provenance, tests, change log and recovery requirements. Require the user to supply the exact stock artifacts; do not bundle vendor firmware or personalized calibration/identity data by default. The XREAL toolkit has an explicit software license and NOTICE, but that license does not license the vendor firmware it operates on. Review provenance and applicable obligations before distributing copied code or derived images; no legal clearance is asserted here.

Use two separate tools: an offline deterministic builder and, only after F3, a narrowly scoped updater. The updater must bind exact device identity, component version and image hash; understand APP/BOOT re-enumeration; preserve independent recovery; and stop rather than blindly retry an ambiguous transfer. Initial work must not replace the bootloader or increase analog panel drive to manufacture brightness headroom.

A feature manifest should say which changes are source-proposed, built, device-accepted and optically demonstrated. A release title must not claim HDR or a refresh rate on the strength of an EDID entry, ACK or a successfully computed CRC.

## IMU contention and HDR feasibility

The control MCU is not a full-rate software video engine. Calculated 3840×1080/60 video already requires 248.832 million pixel updates/s; even an assumed maximum 80 MHz MCU clock gives less than one CPU cycle per pixel. This is not a benchmark and does not mean configuring a hardware LUT is expensive. It means disabling IMU work is not a route to CPU-per-pixel HDR conversion.

Continue the earlier GlassVR provider-lifetime investigation for genuine host or control-plane overhead, without assuming its result determines HDR hardware capability. Stream closure is not proof that on-device sampling/fusion stops. Preserve external tracking and display control as separate services when designing any future lifecycle change.

## Present completion and blockers

Completed: current source review of Pro 2 runtime protocol, XREAL container/update documentation and license notice; the new Pro-header relationship hypothesis; same/neighbouring bridge and Sony-panel comparisons; a hardware-dependent native-HDR strategy; and three fixed arithmetic assertions. The new review is same-author, not an independent hardware or security review.

Not completed: fresh Pro firmware acquisition, checksum hypothesis validation, exact panel manual, full bridge register map, firmware build, successful custom upload, restore test, native-PQ optical test or IMU/refresh benchmark. Network/access failures prevented fresh byte acquisition; they do not indicate vendor removal or device protection. No installation, device write, flash, purchase or outreach occurred.

The next direction is specific: **validate the Pro container and component map, then find a real transfer-processing mechanism, before designing a deployable patch.** This keeps device extension first while distinguishing a promising implementation strategy from a firmware release that is ready to ship.
