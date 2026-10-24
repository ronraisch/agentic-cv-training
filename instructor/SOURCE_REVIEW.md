# Prioritization and source map

This revision adapts the active source collection to a six-week Peanuach researcher route. It
preserves difficult discussion questions while removing duplicate learning routes and unrelated
breadth. Only a brief first-session fundamentals screen remains; subsequent live time is for
challenging reasoning. The complete original question banks remain unchanged in Drive.

## Source scope

[Original collection](https://drive.google.com/drive/folders/1ZfbxunFLoea6JsUIbAiRbDgrkumhGDDA)

Read the current learner and mentor folders and the newer developer primer. The Old 2021-2024
and Archive folders were excluded. The Papers folder was listed for context; its individual papers
were not reviewed as new primary teaching sources in this revision. No video was watched and no
original total watch time was measured. The original outline labels infrastructure as two days,
Python as two to three weeks, CV as two weeks, ML as two weeks, DL as three weeks and papers as
one week. Taken sequentially that is roughly 10.4-11.4 working weeks; it is not an empirical
completion-time estimate. This revision cannot compress all of that unchanged into six weeks.

| Current source | Source link | How it informs this revision |
|---|---|---|
| Training Program Outline New 2025 | [Outline](https://docs.google.com/document/d/1E1C1CqXIUrfuGw2EZoDsALJKG9CyYNew/edit) | Overall outcomes and live progress document; reduce duplicate broad courses |
| Advanced Python Training | [Python](https://docs.google.com/document/d/10i3uoZeVV98XpXxplrF0VUhZwJiyUWch/edit) | Type hints, useful decorators and concurrency reasoning |
| Machine Learning Training | [ML](https://docs.google.com/document/d/1v6KsRgMbj395X2sIQ27RsVnfX_1Kq9O_/edit) | Keep evaluation and small-model reasoning; narrow algorithm breadth |
| Deep Learning Training | [DL](https://docs.google.com/document/d/1ZWM5zmbQNZdYHGjkpCE9XgowJWRWLbnF/edit) | Stanford 2025 concepts, PyTorch, SSL and vision-language |
| Computer Vision Training For Shampooer | [CV mentor](https://docs.google.com/document/d/1FpQhX4xTDs_u8Hq6vXZfXJ9ik-ZbPBkp/edit) | Cost-effective deep sessions; geometry and failure-case questions |
| Machine Learning Questions | [ML mentor](https://docs.google.com/document/d/1cWml7hRyFPYkNQa3SNovhYCcBoUPOxrs/edit) | Prevalence, feature scaling, tuning, ensembles and interpretation |
| Deep Learning Training For Shampooer | [DL mentor](https://docs.google.com/document/d/1AXFN3EvWeFNezszdmS0xXbSZh-UayCKQ/edit) | Trainee teaches; precise terms, proofs and difficult follow-ups |
| Developer reading primer and comprehension | [Reading](https://docs.google.com/document/d/1kfB7PPhGRB0rec8vl3RLtxBY4rXFg7ga/edit) and [questions](https://docs.google.com/document/d/1LbndORHfzAbLItPqh9-5_sOUaSkYPpNc/edit) | First-session screen/reference only, not an added researcher course |

## Keep and deepen

Keep numerical/data contracts, measured correctness, software boundaries and disciplined agent use.
For CV keep filtering, Hough lines, homogeneous coordinates, affine/projective transforms, feature
matching, robust estimation and inverse warping. Connect these to the plate/stitching tasks.
For ML keep generalization, grouped evaluation, prevalence/imbalance, calibration, simple models,
SVM/tree/boosting intuition, feature interpretation and artifact identity. For DL keep gradients,
CNN/receptive-field intuition, normalization/inference, attention/ViT, transfer/SSL/embeddings,
segmentation, video/time and vision-language. Ask deeper questions on these selected concepts.

## Merge repeated material

Teach linear/logistic models, optimization and regularization once; use later sessions to reason
about a new counterexample. Choose one NumPy/Pandas diagnostic route, not multiple tutorials and
exercise banks. Keep one current Stanford 2025 explanation or local substitute per DL concept;
legacy Michigan 2019 links become reference-only. A source slide deck, summary and lecture are
alternative ways to learn, not three cumulative assignments.

The developer primer explicitly aims for conversational basics and overlaps heavily with the
researcher route. Use it to diagnose gaps in the first ten minutes, not as an extra mandatory
5-6-hour module for every researcher. Preserve the source guides' instruction to avoid slide replay.

## Move out of the mandatory six weeks

| Source workload | Decision | Why and replacement |
|---|---|---|
| Full beginner Linux/Python route | Diagnostic plus targeted remediation | Relevant environment checks and small code counterexamples |
| Many overlapping NumPy/Pandas exercises | A few independent contract failures | Same failure reasoning applied in the real monorepo |
| Two long clean-code videos and shape-rendering final | Remove from core | Code review and current labeling request replace detached practice |
| Concurrency benchmark combinations and Streamlit dashboard | One bounded concurrency example; dashboard optional | Team stack is React/TS and Python API |
| Full broad Udacity CV unit list | Selected geometry/filter concepts | Hough rectification and two-image stitching provide actual use |
| Every ML algorithm notebook and extra reading | Keep small representative models | Tracklets and rescoring with proper evaluation |
| Kaggle leaderboard score target | Remove | Held-out consumer metrics matter more than a fixed leaderboard score |
| Naive Bayes/EM/GMM/spectral clustering deep derivations | Optional role-specific follow-up | Keep basic algorithm/modeling intuition and PCA/clustering overview |
| Entire CS231n course plus assignments 1-3 | Targeted concepts and small framework probes | Existing tasks, tiny-overfit and inference explanation replace repetition |
| Legacy 2019 plus current 2025 videos | Current or local route only | Duplicate historical recordings are not mandatory |
| RNN gate details, generative-model blocks, full 3D/distributed training | Optional | Retain temporal/attention concepts needed by current tasks |
| Whole historical detector paper sequence | One concise family comparison; optional deeper paper | No second mandatory detector capstone |
| Every question in every bank live | Keep full banks as references; select deep chains | Preserve depth under the mentor availability cap |

## Time and depth

Trainee: 28 hours core study, four media/substitute hours, 144 project hours, 12 independent
research-agent hours, 12 reserved mentor hours and 40 infrastructure-buffer hours = 240.
Mentor: normally 80 minutes of contact plus 40 minutes of preparation/review per week = 12 hours
over six weeks. These are planning caps; no measured percent reduction in viewing time is claimed.

The first session uses a ten-minute basic screen, a 30-minute plotting-skill check and five minutes
of next steps. Later sessions use two substantial chains: derivation/assumption, counterexample,
empirical check and uncertainty. Difficult questions are retained in [DEEP_DISCUSSIONS.md](DEEP_DISCUSSIONS.md) and the
original banks. Cut repeated content and breadth before reducing a deep discussion to definitions.

## Answer-key care

Some source explanations are useful prompts but should not be copied as universal answers. The
new mentor guide changes neither original file. Review these issues before assessing a trainee:

- Bootstrapping resamples data; boosting is sequential learner construction. Do not conflate them.
- Rescaling inputs can reparameterize equivalent unregularized least-squares predictions; it also
  affects coefficient units, conditioning and regularization. Avoid a blanket answer that the
  prediction must change simply because the features were normalized.
- Support-vector counts are not universally D+1 or a fixed fraction of samples. Test model/data
  assumptions rather than expecting an unsupported fixed number.
- In standard decoder cross-attention, decoder states supply queries and encoder memory supplies
  keys/values. Self-attention without positions is token-permutation-equivariant; pooling can yield
  an invariant summary. Be precise about which output is being discussed.
- Cross-entropy training does not guarantee probability calibration. BatchNorm placement, CNN/ViT
  superiority and global pooling behavior depend on architecture/data; avoid universal claims.

Primary reference checks: [ensemble methods](https://scikit-learn.org/stable/modules/ensemble.html),
[linear models](https://scikit-learn.org/stable/modules/linear_model.html),
[SVM](https://scikit-learn.org/stable/modules/svm.html),
[attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.MultiheadAttention.html),
[calibration](https://scikit-learn.org/stable/modules/calibration.html).
These are review aids; assess reasoned conditions and evidence, not agreement with a stale key.

## Storage and language

Tasks, evidence contracts and runnable code remain in Git. Selected reading/viewing and the
curated syllabus can also live in the new Drive workspace linked from README. Each internal cohort
needs an approved local copy/substitute for inaccessible resources. Active repository content is
English rather than fragile mixed-direction Markdown. Original Hebrew material remains in history
and original Drive documents. No original Drive item was edited, moved or deleted.

Creation inside the original parent folder returned 403 insufficient parent permission. The new
workspace was created separately in My Drive; no permission changes were attempted.
