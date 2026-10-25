# Stage 0 — Matt Pocock skills: installation and exposure

The required collection is **Matt Pocock's engineering/productivity skills**. Earlier references
to Matplotlib and Scientific Visualization were a name misunderstanding and are superseded here.
Plotting libraries may still be used in research; plotting skills are not a stage-0 requirement.
A skill supplies instructions, not tools, permissions, dependencies or proof that code works.

Before installing/activating skills, complete [VS Code, personal OpenShift pod and OMP/local-LLM
setup](GETTING_STARTED_INTERNAL.md#required-setup-order). Run the activation experiment in that
OMP environment against the approved local model (currently QWEN 3.8); unsupported skill discovery
or tool calling must be recorded as blocked rather than assumed from file presence.

## Scope and time

Within the existing six-hour guided setup, reserve about 75 minutes for installation, catalog
orientation and one activation experiment. The first week still has a 30-minute mentor teach-back
inside its existing meeting. Spread deeper practice across the existing agent-work, skills,
review and research assignments; do not add another course or require reading every full skill.

1. Skim **names and descriptions** of the entire pinned collection in the [catalog](MATT_POCOCK_CATALOG.md).
   Recognize the stable engineering/productivity set; identify misc, in-progress and deprecated
   entries as such. Do not read all bodies or install everything merely to browse descriptions.
2. Read the selected entry instructions below and their relevant references, on demand, before use.
3. Demonstrate a small coherent workflow, then reuse the remaining skills in later assignments.
   The mentor samples understanding; there is no requirement to execute every skill in stage 0.

## Focused practice

| Skill / family | Required understanding and exercise |
|---|---|
| `setup-matt-pocock-skills` | Configure the approved GitLab or local-file tracker and documentation paths once. Check those settings rather than assuming GitHub access. |
| `ask-matt` (Ask Matt Pocock) | Route three scenarios to a suitable workflow; explain why a tiny fix does not need the largest flow. |
| `grill-me`, `grill-with-docs`, `grilling` | Compare a standalone interview, a repo-aware interview with glossary/ADRs, and the reusable interview primitive. Try a bounded ambiguous request; distinguish facts to inspect from decisions to ask the human. |
| `wayfinder` | Explain how a large uncertain project becomes linked decision tickets. Make a small decision map for the current assignment and explain when to stop mapping and create a buildable spec. No separate project is required. |
| `to-spec`, `to-tickets`, `implement-spec` | Compare conversation-to-spec synthesis, decomposition into dependent vertical tickets, and execution of the ticket graph. Trace one requirement through all three artifacts. These are different stages, not interchangeable spec variants. |
| `implement` | Implement one bounded ticket in the existing research assignment, using synthetic fixtures for checks. Explain test seams, feedback and completion evidence. Contrast with whole-spec orchestration in `implement-spec`. |
| `code-review` | Pin a comparison commit and review requirements fidelity separately from coding standards. Check one plausible but unsupported finding against the actual diff and runtime path. A reviewer assertion is not evidence. |
| `retro` | Use the completed session's trace to propose one environment improvement: navigation, a deterministic check or a justified standard. Verify what failed and avoid adding generic rules that would not prevent it. |

Use the catalog links for exact pinned entry files. Current names are `ask-matt`, `implement`
and `code-review`; do not invent an `implement-code-review` command. For older names/variants,
check the pinned [upstream deprecation note](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/deprecated/README.md) before substituting anything.
The catalog descriptions are discovery metadata; entry instructions govern the actual exercise.

## Closed-network installation

The mentor prepares an approved complete snapshot of [the upstream repository](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/README.md)
at revision `5beb35b040e3de97e54fa9e386d7e42d15c295c2`, including support files, plugin metadata where needed, license and a file-hash
inventory. Read the entry files to discover dependencies between skills; include those dependencies
in a selected installation. For example, grilling and writing/review disciplines may be referenced
by another skill. Keep relative reference files intact.

Install through the actual approved client's supported local plugin/skill mechanism. The upstream
README lists public installers, but those are not closed-network commands. Do not run public npx,
marketplace auto-updates or fetch examples internally. Python packages still use the approved uv
and Artifactory workflow; uv is not a skill installer. Choose one installation mechanism per client
so the same skills are not discovered twice. Do not overwrite existing skills without comparing
versions. Course examples under `.agents/skills/` are separate from the upstream collection.

Run setup in the approved teaching copy, choosing local files or the internal tracker as agreed.
In a fresh session verify discovery, invocation and the exact loaded path/revision. Copying files
is not activation evidence. Record BLOCKED with owner if the client cannot load the bundle.
Upstream workflows can write tickets, commit or delegate: configure teaching destinations and use
only actions authorized for the exercise. Unsupported tools/subagents must be reported, not faked.

## Teach-back and evidence

Use 5 minutes for skill versus tool/package and invocation modes; 10 for the chosen workflow and
its artifacts; 10 for an incorrect choice, unsupported claim or excessive grilling; 5 for source
pin, activation evidence and a case where no skill is useful. Record the source revision, catalog
orientation, selected full reads, loaded trace, sanitized artifacts and remaining blocked checks.

## Required practice inside existing assignments

The following rows define the required practice for the six-week route. Perform them on the
current assignment. These planning caps replace work already in the named allocations; they do
not add hours to the 240-hour syllabus.

| Selected practice | Where and time already allocated | One acceptance artifact |
|---|---|---|
| Context practice: compare broad versus selected context on the same tiny, unresolved task, with the same starting commit/model and acceptance example | Up to 45 minutes of week 2's two-hour research-with-agent slot, replacing another agent-method exercise | Two session summaries with correctness, one unsupported claim checked, and available counters; no causal performance claim |
| Skill practice: ask-matt routing, a bounded product interview, one requirement through spec/ticket/implementation, then retro | Up to 60 minutes within the 24-hour labeling assignment, replacing its ordinary planning/handoff work | A linked requirement/ticket/diff/evidence trace and one justified improvement; explanations of wayfinder and whole-spec orchestration need no separate project |
| Review practice: review one existing MR against its pinned base and check one plausible finding with a counterexample | Up to 45 minutes within the 24-hour labeling assignment, replacing its normal MR review | A checked review finding, relevant test result and bounded diff |

No separate repair project, mandatory skill rewrite or additional capstone is required by these
references. Internal skill/MCP discovery, success,
failure and fallback remain part of stage 0's existing readiness checks; unavailable tools are
marked BLOCKED with an owner. Do not repeat their walkthrough for each worksheet. The optional
Torch example is used only if assigned. Read selected skill bodies when needed, not all at setup.
If the approved local model exceeds a practice cap, narrow the example with the mentor and record
the limitation; do not consume a separate standalone lab budget silently.

Recommended extras, not another mandatory deep-reading list: `diagnosing-bugs` for a reproducible
failure, `tdd` for behavioral feedback, `handoff` for transfer, and `wait-what` when an explanation
is unclear. Explain why one of these would help your actual task.

The course specifies installation and verification; it does not claim the collection is installed
or activated in the team's internal client.
