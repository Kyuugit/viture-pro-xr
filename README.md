# Original VITURE Pro XR — device extension

This repository owns implementation, decisions and experiments for the **original VITURE Pro XR**. Evidence remains in [the existing bin archive](https://github.com/Kyuugit/bin/tree/main/viture-pro-xr-hdr-refresh-20261029). GlassVR remains the integration target. Other VITURE/XREAL models are mechanism references, not cross-flash targets.

## Current priority — a selectable 90 Hz full-SBS mode

**Start with [SBS90 implementation direction](SBS90-IMPLEMENTATION-20261101.md).** The owner is parking HDR and prioritizing a firmware switch for 3840×1080/90 SBS. Unlike the unsupported HDR-mode suggestions, this starts from the GlassVR author's exact-original-Pro higher-rate setup: stock SBS selection followed by a CRU timing override. The goal is to make a validated configuration selectable from the glasses themselves, not merely change GlassVR's reported frame rate.

The preferred first patch is an additional SBS90 state and active device-side timing advertisement, retaining stock 2D/SBS60 and existing runtime timing handling where it works. Only modify link or panel timing configuration after identifying a necessary change. This is a justified patch hypothesis, not an implemented image or a claim that EDID editing alone always suffices. The GPU still selects the actual input timing.

| Immediate work | Output |
|---|---|
| Stock firmware access | Official manifest/artifact copies with hashes and exact model selectors; no device dump required for packaged update data. |
| Existing 90 Hz reproduction | Complete timing/encoding/topology/firmware record and correct per-eye output, reusing GlassVR's known method. |
| Smallest firmware change | Actual SBS handler and active EDID/profile map, then a guarded Pro-specific SBS90 state. Preserve stock modes and boot behavior. |
| Deployment and recovery | Understand component transfer, integrity/authentication and independent restoration before any custom upload. |

A new [read-only stock downloader/inspector](tools/stock_firmware.py) uses Python's standard library and never contacts the glasses. Its synthetic checks passed; no real Pro binary was available in this runtime. Fresh vendor downloads failed at DNS resolution, not at a device security check. The [research and source review](https://github.com/Kyuugit/bin/blob/2069e59ca843db1e75ef7ce3b1d753a7208937d6/viture-pro-xr-hdr-refresh-20261029/SBS90-FIRMWARE-20261101.md) and [validation/access record](https://github.com/Kyuugit/bin/blob/e59557882d10df08fb73b221599def3851c1f3ed/viture-pro-xr-hdr-refresh-20261029/SBS90-ACCESS-VALIDATION-20261101.json) distinguish those outcomes.

## Retained corrections

[GlassVR refresh correction](DECISION-GLASSVR-REFRESH-20261101.md): the author documents 90 Hz through CRU and separately reports 95 Hz with connection/firmware dependencies. These are operational leads, not our independent optical qualification and not ceilings. A mode enum, ACK or rendering-cadence setting is not physical full-SBS90.

[HDR hardware correction](HDR-HARDWARE-FEASIBILITY-20261101.md): there is no established selectable PQ/HDR mode or adequate programmable implementation identified for original Pro. Earlier recommendations to select one were unsupported and withdrawn. HDR is now parked for this project, not disproven for other micro-OLED systems. No HDR work is a prerequisite for SBS90.

## History and completion boundary

The [previous project index](https://github.com/Kyuugit/viture-pro-xr/blob/326d633f47be3863998a8d0d070bbbc0fa20afd5/README.md) preserves all earlier research navigation. [Firmware feasibility](FIRMWARE-FEASIBILITY-20261101.md), [device-first decision](DECISION-DEVICE-FIRST-20261101.md), [native-HDR requirement](NATIVE-HDR-REQUIREMENT-20261101.md) and [native-HDR investigation](NATIVE-HDR-INVESTIGATION-20261101.md) remain historical context subject to subsequent corrections. Evidence and prior reviews are preserved in bin.

The acquisition/inspection tool is implemented; the SBS90 firmware modification and custom updater are not. No glasses were connected, flashed or measured. No actual Pro container hypothesis, image authentication, recovery procedure or patch offset was established. Stock firmware access, feature implementation, custom-image acceptance and optical qualification are separate milestones. Research does not authorize hardware writes, installs, purchases or outreach. Keep vendor bytes, calibration and private identifiers out of public commits.
