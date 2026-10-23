# Teaching baseline preparation

These are proposed areas, not implemented paths. Map them to a working teaching system before the cohort.
Keep this map out of the initial learner product brief.

| Area | Suggested location | Prepared baseline |
|---|---|---|
| Labeling | apps/labeling | Rectangle tool, zoom/pan, storage and old annotations |
| Data/API | services/labeling | Versioned schema and held-out migration fixtures |
| Training consumer | training/crops and dataset | Real export/loader and a documented product crop decision |
| LPR | src/lpr and services/lpr | Frozen detector/recognizer, baseline, varied plate examples |
| Image stitching | src/imagery | Overlap pairs plus no-overlap/parallax examples |
| Tracklets | src/motion | Timestamps, motion labels, camera information, group IDs |
| Rescoring | src/rescoring | Frozen predictions, independent GT, GSD/angle conventions |
| Clouds | research/clouds | Available sources/data for proposal feasibility |
| Video | src/video and services/video | Clips, approved encoder weights and service boundary |
| Operations | deploy | Internal image, teaching namespace/route/storage |

Prepare an offline visualization-skill bundle with full references and licenses. The mentor reviews
the two entry files once and rehearses the short activation demonstration before the first cohort.
This one-time curriculum preparation is distinct from the recurring 12-hour mentor budget; record
its actual cost rather than hiding it in learner time.
