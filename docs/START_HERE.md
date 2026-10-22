# Start here: your team inherited ResearchLab

Another research team consumes your retrieval report. Its keys are `sample_id`, `scene_id`,
`split`. Results must remain explainable six months later. A demo works, but the team has reports
of missing records, strange metrics, and unstable inference. Your job is to investigate small,
reviewable changes, using AI while owning every accepted line.

1. Install Python 3.11+ and uv using your approved environment. Run the README setup commands.
2. Create a branch `learner/<name>/lab-00`; capture environment and initial command outputs.
3. Read [the curriculum](CURRICULUM.md), then `labs/00-foundations.md`.
4. Create an evidence directory under `artifacts/<your-name>/` in your working copy.
   It is ignored by default: explicitly `git add -f` sanitized evidence when submitting a PR.
5. Submit one bounded PR per lab, using the PR template. A peer reviews before the mentor gate.

Use AI for most development. Before accepting a change, explain the contract and the failure it
prevents. For the short individual checks, close the agent and use the debugger and docs. These
checks measure comprehension, not syntax recall. You may use Python/NumPy reference docs.

## Existing system

`cli` -> `sources` -> Pandas metadata/embedding join -> NumPy ranking -> JSON report.
`HTTPClient` is the transport boundary. `torch_model` is an optional independent embedding path.
`tools/mcp_server.py` exposes a bounded synthetic catalog to a coding-agent client.
Data is synthetic and tiny; `tools/generate_data.py` generates larger local metadata.

Do not load instructor solutions into the agent. In an assessment copy they are absent.
If you are stuck, bring a hypothesis, a minimal failing input, and the last observed output.
A full rewrite is not an acceptable substitute for locating the cause.

## Minimum entry knowledge

Read functions, list/dict comprehensions, imports, exceptions, context managers and basic classes;
run shell commands; branch, commit and inspect Git diffs. Lab 00 routes gaps to practice.
Scientific checks include NumPy axis semantics, array shape/dtype, Pandas joins and missing values.
You are not expected to know design-pattern names before starting.
