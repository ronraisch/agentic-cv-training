# Transfer learning, LoRA, quantization, compilation and parallel execution

[All training](index.md) · [Source coverage](sources.md)

An inference request starts before the model runs and ends after a usable result has been returned. It can involve decoding an image, moving data, running the model and merging predictions. Knowing where time and memory are spent helps you choose which change to evaluate.

<details>
<summary>Jump to a concept</summary>

- [Adapt only what the task needs](#adapt-only-what-the-task-needs)

- [Latency, throughput and memory](#latency-throughput-and-memory)

- [Quantization, pruning and distillation](#quantization-pruning-and-distillation)

- [Compilation](#compilation)

- [Distributed execution](#distributed-execution)

- [Production handover](#production-handover)

</details>

## Adapt only what the task needs

Transfer learning reuses a pretrained representation. A frozen encoder plus a trained head is cheap and isolates adaptation; partial or full fine-tuning changes the representation and may improve domain fit while increasing compute and forgetting risk. Freeze requires checking both which parameters receive gradients and whether stateful layers update buffers. Keep preprocessing and label mapping coupled to the checkpoint.

LoRA parameterizes a weight update as a low-rank product, often `Delta W = scale * B A`, training the smaller matrices while keeping the base weight fixed. Rank limits the update family. Adapter location, scaling and initialization matter. Fewer trainable weights can reduce optimizer state without eliminating the base model's inference memory or forward cost. If merging an adapter into weights, verify that the resulting predictions match under the intended precision.

### Choose which parameters you need to change

Suppose an encoder already produces useful vehicle embeddings, and you receive labels for a small set of categories. A linear head on frozen embeddings is a reasonable first comparison. You can train the head without updating the encoder and can cache the embeddings when preprocessing and encoder weights stay fixed. If the errors show that the needed distinctions are absent from those features, updating part of the encoder may help.

Low-rank adaptation changes a selected weight matrix by adding a product of two smaller matrices. For a d-by-d weight and rank r, a pair of factors has 2dr entries instead of d². With d = 512 and r = 8, that is 8,192 trainable entries for the update rather than 262,144 entries for the original matrix. The base weights still need to be available. The parameter count of the update is therefore a statement about what is trained or stored as an adapter. It does not by itself establish inference speed or total training memory.

Compare a frozen head and an adapted model on the same independent sources. Report which layers were trainable, what data they used and how the resulting artifacts are loaded in the consumer.

### Self-check

You train only a linear head on frozen, unchanged embeddings. Which work can be reused across head-training runs on those inputs?

- A. The optimal head weights for every label set

- B. The test labels as training data

- C. The computed embeddings

- D. A different encoder's incompatible outputs

<details>
<summary>Show answer and explanation</summary>

**C. The computed embeddings**

Fixed preprocessing and encoder weights produce the same features, so the features can be cached across head experiments.

</details>

## Latency, throughput and memory

### Two systems can be faster in different ways

A single image request takes 40 ms from arrival to response. At that rate, processing requests sequentially gives up to 25 images per second. A batch of eight may finish in 100 ms, giving 80 images per second once each batch starts. Each image in a batch can still wait at least 100 ms, plus whatever time it spent waiting for the batch to fill.

The first number describes latency for a request. The second describes throughput. A live camera alert has a deadline per frame, while a dataset backfill may primarily care how many images finish per hour. Batch size changes which workload benefits and how much memory the system needs.

Measure elapsed time from the boundary the client uses. If you start timing after preprocessing, you may miss image decoding and resizing. If a GPU call launches asynchronous work, ensure the timed interval includes completion. Keep warm-up and typical requests separate, and examine slow-tail requests if the service has a deadline.

Latency measures time for a request; throughput measures completed work per unit time. Batching may improve throughput while increasing the time an individual request waits. Measure preprocessing, transfer, model forward, decoding and output merging separately and end to end. Synchronize asynchronous GPU work correctly for timing. Record warm-up, batch/shape distribution, hardware, precision and memory peaks. A FLOP estimate is not a latency measurement.

### Measure one request before changing one component

Suppose an image arrives, is decoded and tiled, passes through an encoder and then has its overlapping detections merged. Record a wall-clock duration around the whole path and separate timings for stages that you can measure reliably. Device work can be asynchronous. A timer around the Python call alone may measure submission rather than execution if the work is still running after the call returns.

Run representative image sizes and record warm-up conditions, batch sizes and queueing. A batch can increase images processed per second while making an individual request wait for the batch to fill. Throughput and latency therefore answer different questions. Memory also needs its own measurement because a larger batch may improve throughput until it exceeds the device budget.

Once the slow stage is known, compare a single change with the same inputs and output-quality criteria. For example, a faster encoder may have little effect when merging dominates. A change in tiling can speed both stages and still harm recall of tiny objects. Measure the tradeoff that the application would actually experience.

## Where an inference request spends its time

Consider a request with illustrative timings of 25 ms for preprocessing, 10 ms in the model and 65 ms for postprocessing. Halving model time reduces the total from 100 to 95 ms.

![Make inference twice as fast. Save 5 ms. Preprocess: 25 ms; Model: 10 ms; Postprocess: 65 ms](assets/dl-deployment-toy.svg)

The model did become twice as fast, but the user sees only a five-millisecond improvement. Reducing the 65 ms stage has more room to help this workload. Batching, data transfer and queueing can change the picture again, which is why the whole request needs measuring.

Quantization, compilation and adaptation techniques are useful tools once we know which constraint we need to change.

### Self-check

A request spends 25 ms before the model, 10 ms in it and 65 ms afterwards. The model becomes twice as fast. What is the new total?

- A. 90 ms

- B. 95 ms

- C. 50 ms

- D. 105 ms

<details>
<summary>Show answer and explanation</summary>

**B. 95 ms**

Only the 10 ms stage changes. It becomes 5 ms, so the total is 25 + 5 + 65 = 95 ms.

</details>

## Quantization, pruning and distillation

Quantization maps values to a lower-precision representation with scales and clipping ranges. Weight-only quantization, weight-and-activation quantization and mixed precision have different hardware paths. Outlier channels can dominate error; calibration data must represent deployment. Smaller storage does not guarantee faster execution if kernels or conversions dominate. Re-evaluate rare classes, small objects and calibration, not just aggregate accuracy.

Pruning removes weights, channels or structures; unstructured zeros need suitable sparse execution to become a speedup. Structured pruning changes tensor dimensions and may require retraining. Distillation trains a student using a teacher's outputs or features alongside available labels. It transfers the teacher's useful behavior and some errors; independent labels and held-out evaluation remain necessary. Compare the whole student path to the teacher rather than only parameter count.

## Compilation

A model compiler captures or traces computation, transforms a graph and generates/selects kernels. Operator fusion can reduce memory traffic and launch overhead. Dynamic shapes, unsupported operations and data-dependent control flow can cause graph breaks or multiple compiled variants. Compilation is a transformation of execution, not proof of equivalent results. Compare outputs, task metrics and error cases across representative shapes and record compile time separately from steady-state latency.

## Distributed execution

Data parallelism replicates a model and partitions examples; gradients are synchronized for training. Model parallelism places different model pieces on different devices. Tensor parallelism divides operations, while pipeline parallelism divides layers/stages. Communication, synchronization and idle bubbles can limit speedup. A larger global batch changes the training experiment unless learning-rate/schedule choices are reconsidered. Mixed model/data strategies require a clear accounting of replicas, batch and state.

A distributed sampler must avoid unintentionally duplicating or omitting examples when evaluating. Aggregate metric numerators and denominators correctly rather than averaging unequal-batch averages. Persist a checkpoint with enough metadata to load it outside the training topology. A distributed job reporting completion is not evidence that the single-device inference consumer reads the same weights.

## Production handover

The final deliverable is an inference-only notebook that loads inputs, preprocesses, constructs/loads the model, predicts, postprocesses and writes outputs using declared packages. Demonstrate it from a fresh process and compare to the verified research path on representative and edge cases. Keep a separate validation entry point for output comparisons and dataset checks. Document observed limitations and missing assets explicitly; do not hide a model download inside inference.

An optimization is useful when the complete inference path becomes cheaper while retaining the agreed behaviour on representative inputs and edge cases. Reloading the saved artifact in a fresh process checks that the delivered system includes the change. The comparison needs both the measured savings and any remaining limits.

<details>
<summary>Original source references and provenance</summary>

Original teaching text covering the cited topics, not a verbatim mirror. These references are provenance; no external reading is required to use this chapter.

- [https://cs231n.stanford.edu/slides/2025/lecture_11.pdf](https://cs231n.stanford.edu/slides/2025/lecture_11.pdf)

- [https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html)

- [https://huggingface.co/blog/hf-bitsandbytes-integration](https://huggingface.co/blog/hf-bitsandbytes-integration)

- [https://huggingface.co/docs/peft/main/en/conceptual_guides/lora](https://huggingface.co/docs/peft/main/en/conceptual_guides/lora)

- [https://huggingface.co/docs/transformers/en/training](https://huggingface.co/docs/transformers/en/training)

- [https://huggingface.co/docs/transformers/perf_train_gpu_many](https://huggingface.co/docs/transformers/perf_train_gpu_many)

- [https://medium.com/geekculture/ai-compilers-ae28afbc4907](https://medium.com/geekculture/ai-compilers-ae28afbc4907)

- [https://www.ultralytics.com/glossary/inference-latency](https://www.ultralytics.com/glossary/inference-latency)

</details>
