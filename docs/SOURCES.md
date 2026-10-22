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

## Six-week researcher route: optional primary references

All required explanations and assignments are local in `docs/lessons/` and `labs/research/`.
These links are optional provenance/reference links, not required network access from inside.
The exact CV course previously sent by the user was not recovered; its module/video mapping
remains open. No invented course coverage or video runtimes are claimed.

| Primary source | Relevant local material |
|---|---|
| [EfficientDet paper](https://arxiv.org/abs/1911.09070) | Lesson 05: BiFPN; reduced teaching architecture explicitly differs from full reproduction |
| [Meta SAM 2 image predictor source](https://github.com/facebookresearch/sam2/blob/main/sam2/sam2_image_predictor.py) | Lesson 02: point-prompt backend; verify the internal pinned version |
| [RF-DETR source and docs](https://github.com/roboflow/rf-detr) | Lesson 06: backend integration; exact API depends on installed revision |
| [GitLab job logs](https://docs.gitlab.com/ci/jobs/job_logs/) | Guided pipeline→job→log navigation; internal UI labels may differ |
| [uv command reference](https://docs.astral.sh/uv/reference/cli/) | Internal Getting Started: network isolation vs cached offline execution |
| [uv certificates](https://docs.astral.sh/uv/concepts/authentication/certificates/) | Internal Getting Started: approved organizational CA trust |

Local lessons are original explanations. They do not redistribute upstream course content,
weights or third-party packages. Technical backend examples are contracts, not verified internal
installations. A mentor records exact internal versions and optional media in the internal copy.
