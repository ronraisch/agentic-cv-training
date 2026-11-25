# Local data and artifact contracts

The bundle root contains `manifest.json`, local `.npy` arrays, `labels.sqlite` and optional
`models/baseline.npz`. Paths in the manifest are relative to that root. Runtime does not fetch URLs.

```json
{
  "schema_version": 1,
  "source": "approved-bundle-release",
  "samples": [{
    "id": "image-000", "kind": "image", "split": "train",
    "group_id": "recording-000", "path": "image-000.npy",
    "sha256": "ACTUAL_FILE_SHA256",
    "annotations": [{"type": "rectangle", "label": "vehicle", "bounds": [8, 7, 40, 25]}]
  }]
}
```

The supported split values are `train`, `validation`, `test`; one source group cannot cross them.
Image arrays are RGB `uint8` `[height,width,3]`. Rectangle bounds use original-image pixel edges
`[x1,y1,x2,y2]`, with finite values, positive area and bounds inside the image. Crop extraction
floors the start and ceils the end; NumPy slices exclude the end. Current classes are `vehicle`
and `building`. `initialize-store` imports initial records; edits persist separately in SQLite.

A persisted image record has `schema_version: 1`, `image_id`, and `annotations` in the format
above. The store uses image identity as its key. Save/reload uses the local API; training reads
the current store, not a UI-only copy or the initial manifest annotations.

Video samples use `kind: "video"`, RGB `uint8` `[time,height,width,3]`, `duration_seconds`, ordered
`timestamps_seconds`, and `targets` in `[road,outdoor,sky_only]` order. The fixture has four sampled
frames at 0/3/6/9 seconds from a ten-second interval. Its model pools frame features; choose a
task-appropriate representation and sampling policy for real assignments.

No pickled arrays or executable model objects are loaded. The NumPy model archive contains both
heads' weights/scaling and a JSON metadata value: schema/feature revision, class/question maps,
training IDs, source/annotation fingerprints and fit history. Inference requires the selected
local artifact and reports its actual SHA-256. See [the baseline](BASELINE.md) for commands and
[offline setup](../setup/OFFLINE_SETUP.md#model-artifacts) for missing-asset recovery.

## Labeling collections

Mount one root, default `data/labeling`. Startup validates all four collections and reports
every missing or malformed collection before opening the app.

| Directory | Required inputs | Source group |
|---|---|---|
| `coco/` | COCO images and instance annotations | Original image or known related capture |
| `video/` | Labeled RGB frames extracted from ordinary-camera recordings | Original sequence or camera; set numerical `timestamp_seconds` on each frame |
| `drone/` | Labeled RGB drone images or frames | Flight, sequence or original parent image |
| `satellite/` | Labeled optical satellite images or tiles | Scene or geographic area, including overlapping tiles and repeat views |

The source provider prepares `manifest.json` in each directory using the schema above, plus a
matching top-level `domain`, a meaningful `source` identifying the dataset/release, and an ordered
`classes` list of unique names. Every entry is `kind: "image"`, including extracted video frames.
Images can be local JPEG, PNG, TIFF or RGB uint8 HWC NumPy arrays. Paths are relative to the collection
and must resolve inside it. Image IDs are unique per collection. Use positive-area original pixel
edge `bounds` and a label from `classes`. Use `annotations: []` for a verified negative image.
Do not use a missing annotation file as a negative. Include at least one labeled object per
collection, and for training include objects in each of the three splits. Source group IDs and
identical image bytes may not cross the supplied splits.

For a source with oriented reference annotations, keep their four ordered image-space corner
pairs as `"obb": [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]` on the record. Keep their axis-aligned
envelope in `bounds` for the HBB starter. Four points must form a convex quadrilateral within the
image. Keep original source IDs and the orientation labels during conversion.

An owner can stage local images and use an index JSON containing `source`, `classes` and
`samples` (each with `id`, `split`, `group_id`, `path` and `annotations`, plus
`timestamp_seconds` for video frames). Generate `kind` and real SHA-256 values from the staged
bytes with:

```bash
uv run --no-sync researchlab-demo import-labels --root /approved/labeling --domain coco --index /approved/indexes/coco.json
uv run --no-sync researchlab-demo check-data --root /approved/labeling
uv run --no-sync researchlab-demo serve --root /approved/labeling
```

Repeat import for the other domains. The app initializes missing SQLite rows from the approved
manifest and preserves edits in the collection's `labels.sqlite`. Give the app a writable
working copy of the collection directories with stable IDs. To train a detector, use
[the YOLO export](DETECTOR.md) to consume a snapshot of those persisted edits. Clip-level
classification uses a separate manifest with clip targets, described above.


## Retrieval catalog

`researchlab --data /approved/catalog --query COMPONENT ...` reads two local CSVs. Supply
`samples.csv` with unique `sample_id`, `scene_id` and `split` columns, and `features.csv` with
the matching `sample_id` and space-separated `embedding` columns. Keep the embedding model and
revision fixed. Pass a finite nonzero query vector with the same dimension as the embeddings.
The read-only MCP catalog uses the same `samples.csv` via `--catalog PATH`.
The SQLite adapter expects a database with a `samples` table and a `split` column.
