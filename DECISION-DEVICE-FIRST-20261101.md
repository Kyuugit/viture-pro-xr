# Decision addendum: prefer extending the original glasses

Date: 2026-11-01. This records the owner's preference to extend the original VITURE Pro itself, and the new same-bridge custom-firmware evidence. It takes precedence over the initial host-mapping-first project priority. The [GlassVR refresh correction](DECISION-GLASSVR-REFRESH-20261101.md) remains in force: reuse the author's high-rate path rather than restarting generic refresh research.

## Direction

**Prioritize device-side capability and firmware investigation. Keep GlassVR as the integration target and calibrated host HDR mapping as a reference/fallback.** Source research comes first; this is not authorization to flash, downgrade, probe hardware, install software or modify the owner's setup.

The strongest new implementation reference is [8796n/nyan-real-firmware-kit](https://github.com/8796n/nyan-real-firmware-kit/tree/e60edfaa4d66fd6de48e13b762010158ed80c76c), which patches matched XREAL Air-family bridge/MCU firmware, including LT7911UXC-family display configuration. It reports full-SBS improvements and coordinated RGB/panel/link changes. This is a genuine device-firmware precedent, not a VITURE port and not an HDR unlock.

The complete evidence, candidate limitations, source pins and self-review remain in [bin: firmware-extension evidence at e50f9b80e7e2ffcfcc43941d80d3b70e25c89ba3](https://github.com/Kyuugit/bin/blob/e50f9b80e7e2ffcfcc43941d80d3b70e25c89ba3/viture-pro-xr-hdr-refresh-20261029/FIRMWARE-EXTENSION-20261101.md). Do not duplicate proprietary firmware here or move the evidence history.

## What changes, and what does not

The owner need not choose between GlassVR and an unrelated movie player. Host-rendered reference patterns remain useful for testing a display extension; they are not the proposed final application by default. A lack of current optical measurements limits capability claims, not source investigation or the priority of the existing GlassVR success.

The recovered GlassVR method comprises an SBS runtime mode, a host CRU timing/EDID override, connection dependencies and reported improvement with an older stock firmware. It does not establish that GlassVR patches firmware itself. The author's 95 Hz SBS report is an operational starting point, not a ceiling or an independently qualified measurement.

The XREAL kit establishes that a closely related bridge can be extended through coordinated firmware configuration. It does not establish a Pro PQ engine, a compatible firmware image, safe original-Pro recovery, or native 10-bit panels. Its RGB888 improvements and higher SBS rate must not be relabelled HDR.

## Prioritized work packages

| Priority | Work | Required output / discriminator |
|---|---|---|
| D0 — exact-model reuse | Continue reconstructing GlassVR's reported CRU/SBS/DP setup and successful firmware identifiers. Reuse the earlier source review's per-eye geometry and tracking/display separation. | Exact timing/EDID, active encoding, adapter/GPU path and same-selector firmware identities when obtainable. Preserve unknowns; do not replace the report with an arbitrary clock limit. |
| D1 — paired firmware map | Map the Pro's own MCU and bridge artifacts and their update/control relationship. Compare legitimately obtained older/newer images of the same selector where possible. | Component boundaries, reachable mode-selection functions, bridge setup, EDID selection and panel initialization, with offsets/source anchors and disassembly-backed interpretation. N6P versus N6PL is not a release regression comparison. |
| D2 — mechanism transfer, not binary transfer | Study the pinned XREAL kit's guarded patches, link-rate selection and coordinated MCU/panel/bridge profiles; correlate against D1. | Specific equivalent Pro mechanism or a clearly documented mismatch. Do not copy XREAL addresses, panel tables or images. Matching diagnostic strings alone is insufficient. |
| D3 — color/transfer feasibility | Identify any reachable programmable gamma, LUT, color-conversion or PQ-handling mechanism in original-Pro hardware/firmware. Compare host SDK/app calls with device handlers. | Explain exactly where encoded PQ would be transformed and what output path/precision it uses. Separate metadata reception from optical transfer. If only SDR/RGB improvements are supported, report that useful narrower outcome rather than declaring native HDR. |
| D4 — IMU resource isolation | Profile/inspect GlassVR provider lifetime independently of display capability. Later compare identical rendering/timing with native IMU service truly enabled versus closed, using a fixed external pose source where appropriate. | Measured CPU/GPU frame time, pose timing and delivered-frame differences. Any gain proves workload contention in that setup, not creation of an HDR engine. |
| D5 — conditional reversible patch prototype | Only after a concrete mechanism, exact image checks, write classification and target-specific recovery are established, propose a separately authorized original-Pro patch. | Minimal guarded patch, deterministic output verification, restoration/recovery procedure and test plan. The proposal precedes any device write. |

D0–D3 source work can proceed without changing the owner's hardware. D4 implementation or testing requires its own scope; an existing provider-lifecycle issue does not make arbitrary firmware writes necessary. D5 is a later decision, not the starting action.

## IMU contention: two separate questions

Original-Pro teardown identifies a control MCU and a separate LT7911UXC video bridge. Reducing IMU work may help MCU scheduling, host CPU/USB overhead or power, but it does not automatically increase video-path capacity or add PQ processing. Shared power/thermal/control-path coupling remains possible and unmeasured. Disabling reports is not proof that on-device sampling/fusion has stopped.

There is a concrete host-side lead in the inspected GlassVR source: HMD activation unconditionally constructs the VITURE provider, whose connection branch opens high-rate pose delivery and starts processing/monitor threads. Merely choosing an external pose source may therefore leave native-IMU work active. Before redesigning tracking or assuming it consumes HDR headroom, establish provider lifetime and profile the actual release. A narrowly scoped improvement would lazily create required services, close unused IMU subscriptions/threads, and preserve independently needed display control.

## Alternatives and exclusions

The exact-Pro vendor corpus and firmware-version differential have greatest target fit. The XREAL kit is the strongest new custom-patch reference. RayNeo Air 4 Pro firmware analysis is useful for discovering existing controls, but its runtime tool is not a successful custom reflash and its additional Pixelworks HDR processor is not established in Pro. The Nordic ECX348ENA panel project and exact-family Linux/Android drivers supply lower-level search fingerprints, not ready replacement firmware.

Pro 2, Luma Ultra and Beast host-driver/protocol projects remain useful comparisons, not evidence of an available original-Pro custom image. No verified turnkey custom VITURE firmware was located in this bounded follow-up. That does not establish that no unpublished or unindexed work exists.

Defer cross-flashing, blind opcode/register scanning, MCU protection changes, erase operations and unsupported downgrade assumptions. Keeping a stock image does not guarantee recovery if the boot/update interface becomes unreachable. Do not infer an HDR result from a builder variable named `HDR`, RGB888 output, a smoother ramp or a changed EDID.

## Outcome gates and remaining decisions

A display extension can be valuable before native HDR is achieved: preserving a better RGB path, stable full-SBS timing, or an accessible existing transfer control are distinct deliverables. Native PQ requires controlled input and optical evidence that localizes the transformation; panel precision remains separate. Higher refresh requires distinct frames in both eyes at the full transmitted raster, with observation duration and conditions recorded.

The next decision is no longer whether the owner prefers host or device work: **device extension is preferred**. Remaining choices concern a concrete intervention once the mechanism is known, acceptable risk/recovery conditions, and available measurement setup. The user does not need to repeat the GlassVR requirement or select a firmware candidate before source analysis can advance.

No new firmware binary was obtained or built in this follow-up, no device test or load benchmark ran, and no original-Pro custom patch, HDR unlock or improved refresh result is claimed. Earlier decisions/reviews remain historical; this addendum changes priorities explicitly and links the new evidence. Future implementation and result records belong in this repository.
