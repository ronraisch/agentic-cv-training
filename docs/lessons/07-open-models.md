# Embeddings, VLMs and open-vocabulary detection

Required before the Part 4 video baseline. Allow two hours of study/self-check within the existing
seven-hour DL block and one hour of probing within the existing 19-hour video baseline allocation.
This replaces repeated representation introductions; it is not another model-training project.

## Three tools, three output contracts

| Tool | Mental model | Input and output | Example reference |
|---|---|---|---|
| Embedder | A learned coordinate system; distance reflects what training made similar | Image/clip to vector; aligned text encoder may put text in a comparable space | [CLIP](https://github.com/openai/CLIP) |
| Open-vocabulary detector | Search the image for regions matching text concepts | Image plus category names/phrase to boxes, scores and phrase associations | [Grounding DINO](https://github.com/IDEA-Research/GroundingDINO) |
| Generative VLM | Condition a language decoder on visual evidence and a prompt | Image/video plus question to generated tokens | [Qwen2.5-VL interface](https://huggingface.co/docs/transformers/model_doc/qwen2_5_vl) |

These are illustrative established references, not a claim that they are the newest/best choice or
already installed internally. A VLM is a broad term; here it means a generative visual assistant.
Some models span several roles, but their particular input/output and evaluation still matter.

## Build an embedding intuition

An embedding is a vector learned for an objective, not a list of named facts. Two images can be
close because of background or appearance even when their tiny objects differ. Image-image
similarity can support retrieval, nearest-neighbor labels or a small learned classifier. A frozen
encoder turns supervised learning into learning a decision rule over its representation; it saves
training work but cannot promise to preserve every detail the consumer needs.

Contrastive image/text learning pulls matched pairs toward one another relative to mismatched
pairs. Alignment enables comparing an image vector with text vectors. An image-only self-supervised
encoder need not have any compatible text encoder. Equal dimensions do not imply a common space,
and vectors from different revisions are not automatically comparable.

For two unit-normalized vectors, cosine similarity is their dot product. For arbitrary vectors,
normalize nonzero vectors first; a raw dot product also depends on vector magnitude. Try the toy
vectors (1,0), (0.8,0.6), (0,1): similarities to the first are 1, 0.8 and 0. Why is 0 not proof of
semantic contradiction? The learned coordinate system and data distribution determine its meaning.
A similarity of 0.8 does not mean an 80% chance that an object exists.

Zero-shot classification compares image/text embeddings for candidate descriptions without fitting
a new task-specific head. Few-shot learning uses a small labeled set, for example prototypes or a
linear head. Fine-tuning updates some encoder weights. Compare their label, compute and maintenance
costs rather than assuming zero-shot always wins. A softmax over two descriptions will distribute
all mass among them, even if neither describes the image; adding a third description changes those
relative probabilities. Independent yes/no questions need not form one mutually exclusive class set.

Check full-image versus crop representations: resizing a large satellite tile can erase a vehicle
while leaving road context. Pooling ordinary-camera frames may capture presence but discard order.
A video encoder's temporal behavior must be checked; averaging image embeddings does not make an
image encoder a video model. Draw the information lost at each resize, crop, patch and pooling step.

## Open vocabulary is not unlimited visual competence

A closed-set detector has a predefined output label set. An open-vocabulary detector accepts text
concepts beyond a fixed downstream label list, using learned vision/language relationships. Text
conditioning does not guarantee that an unseen class, small object, language or domain will work.
Zero-shot on a target benchmark also does not prove absence of related concepts in pretraining.

A global CLIP similarity cannot directly localize all instances. A detector needs spatial evidence
and region outputs; generic segmentation alone does not identify their category. Text grounding
associates a phrase with a region. Inspect the selected model's supported phrase syntax, score and
coordinate definitions rather than treating all detector interfaces as interchangeable.

Compare prompts such as 'car', 'vehicle' and 'red car' on the same image. Record missed objects,
duplicate boxes and attribute errors. Inspect resizing, original-image coordinate mapping, thresholds
and postprocessing. Query-specific scores are not automatically comparable or calibrated. Tune a
threshold on validation data; do not select the best wording on the final test. A score change after
a prompt change can reflect the query, not an improved underlying detector.

## VLM intuition and limits

A typical generative VLM encodes visual inputs into features/tokens, connects them to a language
model, and generates an answer conditioned on text and visual evidence. Image resolution, number
of frames and prompt length affect cost. A structured JSON response makes parsing easier, but does
not make the answer true. A fluent answer can rely on language priors rather than visible evidence.
Generated confidence and token likelihood are not automatically calibrated answer probabilities.

Ask a grounded question, inspect the actual visual input, and compare to independent labels. Include
absent objects, ambiguity and insufficient evidence. Distinguish a load/parse failure from 'no'.
An image VLM shown sampled frames cannot establish an event it never saw. Even a video-capable
model needs valid sampling, timestamps and a temporal test. No grounding/VQA benchmark alone proves
reliability on small remote-sensing objects or ordinary-camera video in the team's deployment.

## Use an open model deliberately

1. Start from the task and required contract: vector retrieval, spatial detection or generated
   answers. Read a model card and a small official inference example for the approved candidate.
2. Record exact repository/checkpoint revision, code/package versions, model and weight terms,
   supported inputs/languages, parameter dtype, device/memory requirements and known limitations.
   Public weights are not automatically an unrestricted open-source release. Parameter count alone
   does not determine activation memory or latency; large images/many frames can be expensive.
3. Prepare an approved local bundle: weights, config, image/video processor, tokenizer/chat template
   where needed, and dependencies. Use that checkpoint's preprocessing and output postprocessor.
   A copied weights file alone may be insufficient. Review custom code before approving execution;
   do not fix load errors by blindly enabling trust_remote_code or installing arbitrary packages.
4. Load from an explicit internal path with the version-supported offline controls. For Transformers,
   [offline guidance](https://huggingface.co/docs/transformers/installation) describes HF_HUB_OFFLINE=1
   and local_files_only=True. Verify the exact pinned API. Check eval mode and inference/autograd scope.
5. Run one known sample, inspect shapes/ranges and original-coordinate outputs, then reload in a
   fresh process. Record artifact/processor hashes and actual executed settings. Encoder or
   preprocessing changes invalidate cached features and may invalidate downstream heads.
6. Measure actual behavior on a tiny held-out set before choosing it. State observed versus inferred
   speed, memory and accuracy; never copy model-card benchmark numbers into a local result table.

## One-hour intuition probe, not three deployments

Reuse [the prepared data](../DATASETS.md#embedding-vlm-and-open-vocabulary-probe): about 12-20 COCO
images with existing annotations, a few small-object DOTA examples and a few already assigned
ordinary-camera clips. Separate prompt-development examples from a small untouched check set.
This is an illustrative sanity check, not a statistically reliable benchmark or another dataset.

- Spend 20 minutes on a real approved local embedder: encode a tiny gallery, normalize vectors,
  retrieve neighbors for an image/text query if supported, and vary candidate descriptions. Compare
  a full image with a crop. Report a counterexample, not just a successful match.
- Spend 20 minutes tracing a prepared open-vocabulary detector and VLM result on the same images.
  If approved runtime/resources exist, run them; otherwise inspect mentor-supplied saved outputs
  with their exact inputs, prompts, model/processor revisions and generation/postprocessing settings.
  Identify boxes versus vectors versus generated text, including one miss or unsupported claim.
- Spend 20 minutes recording which tool fits three concrete questions, where evidence was lost,
  the fresh-load smoke result, one failure and the next falsifying experiment. Explain it without
  the agent. A supplied output is evidence about that saved run, not a run performed by the trainee.

Keep this exercise separate from later product releases: it introduces model families without
revealing future video questions or prescribing a VLM solution. Use the agent to build a diagram,
challenge a 'similarity = probability' claim and design a counterexample, then verify independently.
A missing approved model bundle is a preparation block, not permission to fabricate successful runs.

## Selected primary references

Read the indicated excerpts within the two-hour cap, not entire repositories or papers:

- [CLIP official README](https://github.com/openai/CLIP): inference/features and zero-shot example.
- [Grounding DINO interface](https://huggingface.co/docs/transformers/model_doc/grounding-dino):
  overview and one image/text example with postprocessing; source implementation linked above.
- [Qwen2.5-VL interface](https://huggingface.co/docs/transformers/model_doc/qwen2_5_vl):
  one multimodal input/generation example; trace the processor and actual image/frame input.
- [Transformers offline installation](https://huggingface.co/docs/transformers/installation):
  only the offline/local-files section. Mirror approved excerpts internally before the cohort.
