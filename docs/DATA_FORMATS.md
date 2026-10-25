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
[offline setup](OFFLINE_SETUP.md#model-artifacts) for missing-asset recovery.
