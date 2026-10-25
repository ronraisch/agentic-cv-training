# Local detector

The repository includes `researchlab.detector.network`: two convolutional blocks and a learned
head for one box, two classes and object presence. It accepts RGB float32 BCHW arrays of shape
`(N, 3, 32, 48)` in `0..1`, returns normalized `xyxy` coordinates, class probabilities and object
probability. The classes are `vehicle` and `building`. Filter by object probability before using
a returned box. This baseline supports at most one object per image; it is not a multi-object,
open-vocabulary or license-plate detector.

Install the approved locked `torch` extra using [offline setup](OFFLINE_SETUP.md#detector-runtime).
No dataset or pretrained weights are downloaded. Run:

```bash
uv run --no-sync researchlab-detector smoke --model artifacts/detector/model.npz
uv run --no-sync researchlab-detector evaluate --model artifacts/detector/model.npz
```

The fixture has variable box locations, two foreground classes and empty images. Training uses
160 generated images; evaluation uses 80 images from a separate deterministic seed. `smoke`
trains, saves, reloads and checks held-out localization, class and presence metrics. Generated
images are a plumbing test, not a scientific benchmark. The saved NPZ has NumPy arrays for all
network parameters and JSON metadata; loading does not execute a pickled model.

For an independent input, prepare a local `.npy` float32 BCHW array with the approved loader:

```bash
uv run --no-sync researchlab-detector predict --model artifacts/detector/model.npz --input /approved/data/images.npy
```

`predict_batches` provides bounded-memory inference, used by the CLI. The Python `predict`
function accepts the same image tensor for an individual batch. Outputs remain in resized image
coordinates; a consumer must map normalized coordinates to the original dimensions and retain
image identity and preprocessing information.

## Named external models

The reference lesson's model names are not aliases for this local network. The optional probe
uses [CLIP](https://github.com/openai/CLIP),
[Grounding DINO](https://github.com/IDEA-Research/GroundingDINO) and
[Qwen2.5-VL](https://github.com/QwenLM/Qwen2.5-VL). Their source repositories provide architecture,
checkpoint and processor instructions. To assign that probe, the environment owner must stage
the selected implementation and exact checkpoint revision, compatible runtime, processor and a
local invocation example. Those large-model runtimes and weights are not included here.

For the LPR and frozen-detection assignments, supply the approved detector and recognizer,
weights/class map, representative inputs and their actual local inference command before the
assignment begins. The procedural two-class network cannot substitute for those models. Record
these in [the internal environment map](../templates/internal-environment.example.md), including
artifact hashes and expected paths, and follow [model preparation](OFFLINE_SETUP.md#model-artifacts).
Do not revive superseded detector assignments merely because a historical document named them.
