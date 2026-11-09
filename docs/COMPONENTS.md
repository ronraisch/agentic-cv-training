# Frozen research components

The workspace supplies a plate detector and recognizer, vehicle detector, tracklet producer and
JSONL exports for the LPR, motion and rescoring assignments. The trainee obtains and inspects
the datasets using [the acquisition instructions](DATASETS.md#acquire-a-working-subset), then
implements the assigned preprocessing or learned head. Existing components are in
[components.py](../src/researchlab/components.py).

## Installation and models

On an approved connected workstation:

```bash
uv sync --locked --extra dev --extra mcp --extra components
uv run --no-sync researchlab-components fetch --root .local/models
uv run --no-sync researchlab-components check --root .local/models
```

`fetch` is an explicit model-download operation, not part of inference. It retrieves about
125 MiB from the upstream GitHub releases, verifies the pinned SHA-256 values and writes the
bundle manifest. For an LPR-only bundle, use both commands with the same selection:

```bash
uv run --no-sync researchlab-components fetch --root .local/models --models plate ocr
uv run --no-sync researchlab-components check --root .local/models --models plate ocr
```

On the internal network,
use the transferred bundle at the owner-provided path. All other commands read local assets
only; a missing or different model stops with a recovery command. The lock includes CPU ONNX
Runtime and headless OpenCV. It does not install a detector training framework.

| Component | Frozen implementation | Supported use |
|---|---|---|
| Plate detector | YOLOv9-t, 384 input, end-to-end ONNX export | Axis-aligned plate boxes in original image coordinates |
| Plate recognizer | CCT-xs-v2 global, 64 by 128 RGB input | Uppercase Latin letters and digits, ten slots |
| Vehicle detector | RF-DETR nano COCO, 384 input, ONNX | Bicycle/car/motorcycle/bus/truck classes; axis-aligned boxes |
| Tracklet producer | Greedy same-class IoU association | Constant-frame-rate ordinary-camera video; IDs local to one sequence |

The recognizer has no Chinese province characters. Use Latin/digit plates for this supplied
baseline. CCPD requires a different matching recognizer for full-plate evaluation; the provided
recognizer is not a substitute. The vehicle model is trained on COCO, not DOTA; evaluate its
domain behavior independently. For DOTA vehicle rescoring, predeclare the source-class mapping
and use enclosing axis-aligned GT boxes for this baseline. Do not report oriented-box benchmark
scores from these outputs. A separately approved OBB model can replace it under an explicit contract.

## Image manifest

Create a UTF-8 JSONL file, one image per line:

```json
{"id":"camera-a-0001","path":"images/0001.jpg","scene_id":"camera-a","gsd_m":null,"view_angle_deg":null}
```

`id` is a unique string. Paths resolve relative to the manifest file, or may be absolute. Retain
the original source ID in your data inventory. Optional metadata stays null when unavailable;
do not infer ground truth or physical size from filenames. Keep labels in a separate annotation
file. Inference does not read them. A record is emitted for every decoded image, including zero
detections; a decode error stops the command.

## LPR baseline and crop recognition

```bash
uv run --no-sync researchlab-components lpr --root .local/models \
  --manifest data/imported/lpr/images.jsonl --output artifacts/lpr/raw.jsonl \
  --overlay-dir artifacts/lpr/overlays
```

Each detection includes `detection_id`, `box_xyxy`, detector `score`, recognized `text` and
per-slot OCR confidence. Coordinates are in the original image's pixels. The output also records
model hashes, image identity and dimensions. Confidence is not a calibrated probability of a
correct plate. The raw path crops each detector box and calls `Models.recognize(crop)` on a BGR uint8 HWC crop. The recognizer converts BGR
to its model's RGB format internally; pass OpenCV crops without reversing channels. It does
not perform Hough estimation or perspective rectification.

Use that same recognizer on the result of your assigned preprocessing:

```bash
uv run --no-sync researchlab-components recognize --root .local/models \
  --crop artifacts/lpr/rectified.png
```

Do not replace detector crops with GT corners on the inference path. Preserve the raw baseline
and use the same models/data for the comparison. The geometry and evaluation work remain the
[part-2](../labs/research/02-classical-cv.md) and [part-3](../labs/research/03-evaluation-ml.md) assignments.

## Vehicle predictions for rescoring

```bash
uv run --no-sync researchlab-components detect --root .local/models \
  --manifest data/imported/rescoring/images.jsonl --threshold 0.1 \
  --output artifacts/rescoring/frozen.jsonl --overlay-dir artifacts/rescoring/overlays
```

Keep this output frozen during rescorer fitting. It supplies class, score, box, detection/image
IDs and available metadata, without reading GT. Independently acquired annotations are needed
for matching, misses and evaluation. Lowering the threshold changes candidate recall and must
be recorded; a rescorer cannot recover objects absent from the candidate set.

## Tracklets for motion classification

A **tracklet** is a short fragment of observations linked by a tracker to one apparent object.
The command below exports frames, so assemble the observations for each tracklet by grouping
detections by `(sequence_id, track_id)` and ordering them by timestamp.

```bash
uv run --no-sync researchlab-components track --root .local/models \
  --video data/imported/video/sequence-a.mp4 --sequence-id sequence-a \
  --output artifacts/tracks/sequence-a.jsonl
```

One JSONL row per decoded frame contains `sequence_id`, zero-based `frame_index`, `timestamp_s`,
`fps`, model hash, tracker version and detections with integer `track_id`. IDs restart for each
command; use `(sequence_id, track_id)` as the track identity. Empty frames are retained. This
baseline requires a constant-rate video; timestamps are frame index divided by container FPS.
Convert variable-rate footage with a recorded time mapping before use.

The tracker matches by class and box IoU above 0.3, retaining a track for five missed frames.
It has no appearance model, camera-motion compensation or long-occlusion recovery. Audit the
tracklets and annotate the requested motion taxonomy independently; track IDs are not motion
labels. The exercise trains a motion classifier, not another detector/tracker.

## Upstream models and preprocessing references

- [Open Image Models](https://github.com/ankandrew/open-image-models): YOLOv9 plate export and
  RF-DETR COCO export, with their preprocessing/output definitions.
- [Fast Plate OCR](https://github.com/ankandrew/fast-plate-ocr): CCT-xs-v2 model and
  [Latin configuration](https://github.com/ankandrew/fast-plate-ocr/blob/master/config/latin_plate_config_v2.yaml).
- [RF-DETR](https://github.com/roboflow/rf-detr): detector architecture and model terms.

Retain upstream model/code terms when transferring assets. Public availability does not replace
the team's approval of a model or dataset. Training SAM2/SAM3 services and the later YOLO/RT-DETR
pipeline uses the separate environments specified in those assignments.
