# System map

The working CPU baseline covers image labeling and ordinary-camera video. It uses local
procedural inputs by default and can read approved compatible bundles. See [baseline commands](BASELINE.md).

| Area | Implemented path |
|---|---|
| CLI and installation errors | [demo_cli.py](../src/researchlab/demo_cli.py) |
| Data/annotations/crop loader, training, artifact and inference | [demo.py](../src/researchlab/demo.py) |
| Local HTTP API and image rendering | [demo_web.py](../src/researchlab/demo_web.py) |
| Labeling interface | [index.html](../src/researchlab/static/index.html) |
| Existing catalog/retrieval modules | [pipeline.py](../src/researchlab/pipeline.py), [sources.py](../src/researchlab/sources.py) |
| Shared transport | [http.py](../src/researchlab/http.py) |
| Local CNN detector, fixture, training and inference | [detector.py](../src/researchlab/detector.py), [contract](DETECTOR.md) |
| Optional Torch component | [torch_model.py](../src/researchlab/torch_model.py) |

Annotations persist in the selected bundle's SQLite store. Training consumes current records and
writes an explicit model artifact with feature/class/question versions and data fingerprints.
Inference reports the loaded artifact checksum. The video baseline pools local frame features;
it is not a large pretrained video/VLM system. Image geometry, LPR and later customer requests are
implemented as assigned against approved prepared inputs.

The service binds to loopback. Internal hosting uses approved identity, ingress, registry and
persistent mounts; local success does not verify those integrations. Ordinary ground/handheld/
vehicle-camera video is distinct from airborne/satellite imagery used in separate assignments.
