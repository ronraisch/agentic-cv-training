# Scientific and agent-work pitfalls

This is a general learning checklist, not a solution to product requests. Use an independent input
and a falsifiable explanation. Infrastructure is guided; scientific mistakes need understanding.

| Pitfall | Misleading appearance | Independent check |
|---|---|---|
| Stale documentation | Convincing architecture narrative | Current caller/config and actual request |
| Invented agent API | Professional-looking wrapper | Installed version and real smoke |
| Test copied from implementation | Green suite | Independent oracle and counterexample |
| Swallowed exception | Plausible empty output | Error versus unknown versus negative |
| Color/range/dtype mismatch | Similar-looking image | Known values at each boundary |
| Wrong Hough lines | Strong edges | Plausible boundary geometry and failure rejection |
| Inappropriate homography | Smooth seam | Independent points, parallax and no-overlap |
| Only successful crops scored | Large apparent LPR gain | Full denominator including fallback/failure |
| Correlated splits | Excellent metrics | Video/scene/acquisition disjointness |
| Future feature | Easy motion prediction | Data available at decision time |
| Metadata shortcut | Better held-out rows | Grouped sensor/scene test and ablations |
| Undefined size/angle units | Convincing physical rule | GSD, projection, clipping and convention |
| Ranking called calibration | Better PR | Reliability and target definition |
| Search saved a default model | Successful tuning log | Selected estimator to loaded artifact trace |
| Encoder changed under a head | Checkpoint loads | Representation/schema/cache revisions |
| Training mode during serving | Unstable outputs | Eval plus appropriate autograd scope |
| Frozen hidden component | Loss decreases | Component gradient and parameter update |
| Pixel IoU only for clouds | Good segmentation score | Net compute and object recall after gating |
| Skipped cloud area called empty | Confident consumer answer | Unobserved versus zero detections |
| Sampling removes an event | Clear selected frames | Temporal evidence and event-level test |
| Missing label treated negative | Simple training table | Annotation mask and unknown policy |
| Fluent VLM output | Well-formed answer | Independent truth, parsing and versioning |
| Hidden notebook state | Works for its author | Clean restart and a new input |
| CI green alone | Feeling of completion | Actual commands, skipped tests and scope |
| Mutable image tag | Apparently new deployment | Digest and actual loaded artifact |
| Pod-local storage | Save appeared successful | Persistent read after teaching restart |
| Attractive chart | Apparent model improvement | Units, denominators, uncertainty and consistent scales |
| Skill copied but unused | Assumed guardrails | Actual loading trace and negative trigger |

A valid result may be that a proposed method does not help. Explain what the evidence supports and
what remains unverified instead of producing a more confident story.
