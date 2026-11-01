# Original-Pro SBS90 switch: implementation direction

Date: 2026-11-01. Current priority: make 3840×1080/90 full-SBS selectable from the original glasses. GlassVR remains the application target. HDR work is parked, not declared impossible across all micro-OLED devices. This is a concrete development proposal supported by an exact-model high-rate report; it is not a built firmware patch or a demonstrated custom upload.

## Decision

Retain the vendor firmware and add a narrow SBS90 mode state. The first candidate is to make the known working host-overridden timing available through the glasses' own active SBS EDID/profile and selection handler. Existing stock timing handling may already suffice once a 90 Hz signal arrives; establish that before modifying link/panel initialization. If it does not suffice, map and modify only the specific missing coordinated transition. Do not assume a built-in SBS90 handler, a magic SDK enum or a copyable XREAL patch.

[Supporting evidence, source identities, exclusions and same-author review](https://github.com/Kyuugit/bin/blob/2069e59ca843db1e75ef7ce3b1d753a7208937d6/viture-pro-xr-hdr-refresh-20261029/SBS90-FIRMWARE-20261101.md) remains in bin. It reuses the [GlassVR correction](DECISION-GLASSVR-REFRESH-20261101.md) and historical firmware corpus rather than restarting the survey. The author documents SBS90 via CRU and separately reports 95 Hz; neither is a maximum or our own optical measurement.

## 1. Get the stock artifacts without opening or changing the glasses

Use the official manifest and its selected artifact URLs. The earlier acquisition record identifies N6P/N6PL variants, but they are not interchangeable and neither should be chosen for flashing merely because the name contains Pro.

A new standard-library-only tool is available at [tools/stock_firmware.py](tools/stock_firmware.py). From this repository with Python 3.10 or later:

```sh
python tools/stock_firmware.py fetch N6P --out private-firmware/n6p-source
python tools/stock_firmware.py fetch N6PL --out private-firmware/n6pl-source
```

These download both variants for analysis, not deployment. No glasses connection, driver installation or administrator privileges are required. Each destination must be new. The tool saves stock bytes, manifest and a metadata report and puts `*` in a local `.gitignore`. Keep proprietary payloads private.

For files already downloaded, including a historical stock copy:

```sh
python tools/stock_firmware.py inspect /path/to/stock.bin
```

The report compares the 29 October hashes and tests the XREAL-style container CRC only as a hypothesis. Unknown hashes are analysis inputs, not approved patch baselines. EDID-header candidates are not assumed active. The inspector neither modifies a firmware input nor implements a flasher.

Fresh downloads failed at DNS resolution in this runtime. Synthetic parser/CRC/EDID checks passed, but no actual Pro image was tested here. The tool is an implemented acquisition/inspection aid, not proof of current vendor download availability or of a validated Pro container. If manifest syntax changes, it stops instead of executing JavaScript. A browser's network log can identify the exact official artifact request without initiating an update; do not press Update just to obtain traffic. If a DP artifact is only discoverable through another path, record that gap rather than guess its URL.

## 2. Establish the exact state we want the firmware to reproduce

Use the GlassVR author's documented stock SBS + CRU approach as the baseline. Export the factory and effective SBS EDIDs and record the complete working 90 Hz timing, transmitted pixel format/depth, connection path and exact firmware. Keep 2D and SBS60 restore paths.

Before designing a patch, establish correct eye splitting and actual distinct frame delivery in both eyes at 3840×1080. A requested Windows rate or GlassVR cadence is not the physical result. GlassVR uses 1920×1080 per-eye dimensions with stereo enabled for full-width SBS; set its rendering cadence to match the actual physical rate. Do not treat the GlassVR field as a firmware or physical-mode setter.

## 3. Trace and implement the smallest change

Map the existing physical-button/HID SBS handler to the active bridge mode, EDID selection/building and panel configuration in hash-identified stock images. Separate ARM MCU code from any embedded or separately transferred bridge code/data. Use existing strings and EDID patterns only as search anchors. Do not blindly edit every 60 Hz descriptor or combine 2D90 and SBS60 tables.

Proposed new behavior, not a statement about stock firmware:

- Preserve the stock 2D state and SBS60 state, and introduce an additional explicit SBS90 state.
- In SBS90, advertise the validated full-SBS 90 Hz timing through a mode-specific EDID/profile, with appropriate checksums and unchanged unrelated identification/audio information.
- Reuse the existing mode-change notification so the source re-reads the active profile. Apply additional bridge/panel settings only when their necessity and semantics have been established.
- Keep a blind button escape to stock 2D/SBS60 and initially retain the original power-on default. Choose an actual unused gesture only after mapping existing button functions.
- Do not save persistent mode preferences or touch calibration/bootloader/protection regions in the first prototype.

The GPU still chooses the transmitted timing. A preferred 90 Hz profile is not a universal command to the host; an optional host mode-selector may be needed where the OS remembers 60 Hz. That helper would select a mode advertised by the device, not supply the firmware functionality through a permanent CRU override. Success must be checked against the active signal and both-eye output.

An EDID/mode-state-only patch is the first hypothesis because stock higher-rate operation is already reported. Coordinated MCU/DP/panel changes are the next scope only if needed, as demonstrated in the XREAL family. XREAL register values, firmware bytes, protocol commands and recovery behavior are not transferable assumptions.

## 4. Qualify writing separately from constructing bytes

The stock updater provides a real USB update path with MCU/DP stages; it does not establish acceptance of a custom local file. Map model selection, component destinations, integrity/authentication, re-enumeration and failure handling from official updater code before writing a replacement tool. A checksum match cannot prove modified-image acceptance. The directory name `dfu-util` does not establish standard USB DFU compatibility.

First produce a no-change parse/rebuild that is byte-identical to the known artifact. Then build a guarded minimal change, rejecting unknown baselines and unexpected original bytes. Only after a target-specific independent recovery path is established should a separately authorized modified-image trial be considered. Keep bootloaders and per-unit information intact. A button fallback for a bad display mode does not recover corrupted firmware.

Use SWD or direct bridge-flash access only as a later hardware investigation if the official path is inadequate and access/recovery is understood. Do not begin with protection removal, mass erase, cross-flashing or a full firmware rewrite. No hardware access is authorized or performed by this plan.

## Completion and immediate outputs

Completed now: source-backed strategy, current model/protocol exclusions, read-only acquisition/inspection implementation and synthetic tests. Not completed: fresh Pro artifact acquisition, validated component/checksum map, active SBS handler address, custom updater, deployed patch, recovery qualification or optical SBS90 result.

The immediate useful deliverables are (a) exact stock MCU/DP artifact identities and map, (b) one verified original-Pro 90 Hz timing/configuration, and (c) a minimal mode-state/active-EDID diff tied to that configuration. Firmware acceptance/recovery is the key deployment blocker; target-specific timing evidence prevents the feature patch from becoming guesswork. No additional HDR research is a prerequisite.
