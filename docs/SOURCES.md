# Sources and scope (reviewed 2026-10-22)

This repository is original teaching material. No upstream slides, exercises or code were copied.
Links are optional selected reading; local guides and runnable assignments stand on their own.
Public syllabi describe intended content, not independent evidence of course effectiveness.

| Source | What informs this course | Local adaptation |
|---|---|---|
| [Penn: Software Development with AI Agents](https://agent-p.org/courses/cis-3990-001-fall-2026/public) | Inherit existing software; architecture, specification, review, validation, responsibility | ResearchLab, labs 01/09/11, individual defense |
| [Stanford CS146S](https://themodernsoftware.dev/) | Context/capabilities, MCP, agent skills, executable specifications, iterative workflows | Labs 06–08, AGENTS.md, task specs and session evidence |
| [Carpentries Intermediate Research Software Development](https://carpentries-incubator.github.io/python-intermediate-development/) | Collaborative environment; automated tests/CI; design/refactoring; review; reuse/release; lifetime maintenance | Labs 00–04 and 09–11, CI, packaging, peer handover |
| [Agent Skills specification](https://agentskills.io/specification) | SKILL.md metadata, conditional loading, references | Example skills and validator |
| [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) and [server guide](https://modelcontextprotocol.io/docs/develop/build-server) | Real stdio server and protocol client | Pinned 2.3.0 SDK; metadata tools and protocol check |
| [NumPy docs](https://numpy.org/doc/stable/) | Shapes, views/copies, numerical behavior | Lab 02 |
| [Pandas merge](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html) | Cardinality validation | Lab 03 |
| [PyTorch inference mode](https://docs.pytorch.org/docs/stable/generated/torch.autograd.grad_mode.inference_mode.html) | Autograd versus module evaluation state | Lab 05 |

Carpentries materials are CC BY 4.0; their GitHub repository is
https://github.com/carpentries-incubator/python-intermediate-development/ . We link rather than
redistribute their lessons. Penn/Stanford pages being publicly readable does not imply unrestricted
reuse of all course content. Check original licenses before importing materials. This curriculum
covers selected ideas, not every lesson taught in either university course. No endorsement implied.


## Peanuach route — current optional primary references (2026-10-23)

Required explanations are local in docs/lessons; public URLs below are optional provenance,
not required network access. No upstream lessons or code were copied into these texts.

| Primary reference | Local use |
|---|---|
| [OpenCV Hough tutorial](https://docs.opencv.org/4.x/d9/db0/tutorial_hough_lines.html) | Classical CV: line estimation, parameters and segment/line distinction |
| [OpenCV feature matching and homography](https://docs.opencv.org/4.x/d1/de0/tutorial_py_feature_homography.html) | Classical CV: matches, robust estimation and geometric checks |
| [OpenCV homography concepts](https://docs.opencv.org/5.0/tutorials/features/homography/homography.html) | Planar approximation and limits of image stitching |
| [scikit-learn calibration documentation source](https://github.com/scikit-learn/scikit-learn/blob/main/doc/modules/calibration.rst) | ML: ranking vs probability calibration and held-out fitting |
| [GitLab job logs](https://docs.gitlab.com/ci/jobs/job_logs/) | Guided pipeline/job/log navigation only |
| [uv CLI](https://docs.astral.sh/uv/reference/cli/) and [certificates](https://docs.astral.sh/uv/concepts/authentication/certificates/) | Internal setup prepared by the mentor |

Internal package versions can differ from these moving documentation pages. Validate installed
APIs against the approved internal version. Cloud literature review and model comparison are
trainee tasks: the curriculum does not claim that a current winning architecture was identified.
The exact prior CV course and the mentor document in Drive have not been located/read; their
content and session procedure are not claimed to be incorporated. Internal Confluence is for
team context; no internal content is exported to this public repository.
