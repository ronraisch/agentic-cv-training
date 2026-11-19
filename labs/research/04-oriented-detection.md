# Upgrade the detector to oriented boxes

## Start here

Run [the YOLO11 baseline](../../docs/DETECTOR.md) on the labeled satellite collection in the
[local data mount](../../docs/DATA_FORMATS.md#labeling-collections). Bring a plot, an image
containing close or diagonal objects, and a trace from the model output to the stage 1 annotation UI.

## Make the upgrade

Connect a trained YOLO11n-OBB checkpoint to the stage 1 annotation flow. Use the independently
labeled corners as oriented ground truth. Verify a fresh prediction, overlay alignment in original
pixels, and the save/reload path. Handle angle equivalences, image resizing, multiple detections,
empty output, and objects near image edges. Keep existing axis-aligned records readable.

Show the mentor when tighter geometry helps remote-sensing interpretation. Bring a crowded scene
or a scene with diagonal elongated objects, and one where orientation is ambiguous or unnecessary.
Compare overlap, orientation and the practical consequence for interpreting the scene.

## Run the experiments

1. Save the baseline arguments, split IDs, learning-rate and loss curves, and localization plots.
   Inspect batch composition by group, class and resolution. Pick one diagnostic that could
   distinguish optimization behavior from a change in the data the model sees.
2. Change one training choice at a time. Compare fixed-LR SGD to a modern alternative with an
   explicit schedule. Test whether shuffled or better-mixed batches affect convergence or rare
   classes. Save actual LR and per-loss curves with the same initialization, seed and budget.
3. Compare the example split to a recording/scene-level split. Check overlap, class and small-object
   coverage, and any shift in the held-out distribution. Use the same fixed test groups for the
   final comparison.
4. Compare ROC AUC at IoU 0.90 with a detection PR curve and AP at justified IoU thresholds.
   Include missed objects and choose a useful operating point for the task. Use oriented overlap
   for the OBB result and a common comparison geometry when making direct HBB/OBB claims. Separate
   matching IoU from NMS IoU and confidence. Show how the conclusion changes by object size or scene.
5. Walk through the plots with the mentor. Bring one failure case, one conclusion the data
   supports, and one result that needs a larger or more representative sample. Keep run IDs,
   exports and checkpoints so the mentor can reproduce the comparison.

[Detection heads](../../docs/reading/dl-detection-head.md) ·
[Optimization and reliable training](../../docs/reading/dl-training.md) ·
[Metrics](../../docs/reading/ml-metrics.md)
