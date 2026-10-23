# Guided setup in the internal network

Goal: use the correct project environment in VS Code/Jupyter and demonstrate a known request,
persisted output and accessible team documentation. The mentor helps throughout. This is teaching,
not a DevOps examination. The internal stack already exists; do not rebuild infrastructure.
The mentor supplies actual URLs, approved identities, versions and fixture outputs in
`templates/internal-environment.example.md` inside the internal copy only.

For every check record action, expected output, actual output, PASS/BLOCKED and escalation owner.
Do not commit tokens, kubeconfig, credentials or internal-only addresses to the public repository.

## GitLab and VS Code

Open the internal project, use its approved Clone URL and open the directory in VS Code.

```bash
git status
git remote -v
git log -1 --oneline
```

Expect the chosen branch/commit, clean tree and internal remote. The README must match the selected
revision. A missing repository usually means the wrong directory; DNS/timeout needs network help;
certificate issues need the approved organizational CA; permission denied needs the correct identity
and project access. The mentor helps rather than grading your infrastructure troubleshooting speed.

## Python and uv through Artifactory

```bash
python --version
uv --version
```

ResearchLab needs Python 3.11+. Use the approved internal Python/uv, index, CA and internal lock.
The public lock can embed public artifact URLs: adding an index flag alone does not prove an
installation stays internal. The mentor validates a clean internal environment before the cohort.
Do not re-lock arbitrarily or download a public installer from the closed network.

After the approved internal configuration is ready:

```bash
uv sync --extra dev --extra mcp --locked
uv run --no-sync python -c 'import sys, numpy, pandas; print(sys.executable); print(numpy.__version__, pandas.__version__)'
```

Expect successful sync, the project interpreter and approved versions. 401/403 suggests repository
access; TLS suggests trust configuration; a missing package requires checking version/platform/index.
Do not bypass TLS or silently change versions. A public-host request means configuration needs
review. `--offline` prevents fetching uncached packages even from internal Artifactory; use it only
when testing an already-prepared cache. It is not synonymous with a closed internal network.

## VS Code interpreter and debugger

Use Python: Select Interpreter to select the project environment. Set a breakpoint in the teaching
pipeline and run the mentor's debug configuration. Expect the same sys.executable as the terminal
and a breakpoint showing a meaningful array shape. If terminal imports work but editor imports fail,
check the interpreter/remote side before installing anything. Extensions come from approved resources.

## Jupyter kernel and restart

Open Jupyter or a VS Code notebook and choose the project kernel. Jupyter/ipykernel are provided by
the approved environment, not assumed to be installed by ResearchLab's current extras.

```python
import sys
import numpy as np
print(sys.executable)
x = np.array([[3.0, 4.0]])
print(x.shape, np.linalg.norm(x, axis=1).tolist())
```

Expect the correct interpreter, `(1, 2)` and `[5.0]`. Save, restart the kernel and run all cells.
Success requires identical meaning after restart, not merely a browser page that opens.
Wrong imports usually mean the wrong kernel; failed save requires checking path/permissions.
Do not copy a token-bearing notebook URL into the MR.

## Visualization skills

Complete [SKILLS_STAGE0](SKILLS_STAGE0.md). Install the approved Matplotlib and Scientific
Visualization instruction directories with their support files. Verify actual loading and a
negative trigger, not only file presence. Run one tiny static plot in the approved environment.
Record a blocked activation honestly. The first mentor session includes the 30-minute skill check.

## Known code smoke

```bash
uv run --no-sync researchlab
uv run --no-sync pytest
uv run --no-sync python tools/check_mcp.py
```

For the preserved starter, expect a fixture JSON report, five smoke tests and MCP discovery/calls
plus rejection of an invalid limit. An intentional invalid-input error in that check is expected.
The teaching code has deliberate defects; a green smoke suite is not proof of full correctness.
Record the actual revision and compare with mentor-provided outputs if the baseline changes.
For the prepared Peanuach system also demonstrate UI/API/save/reload on its known fixture.
If that system has not been prepared, mark the corresponding gate blocked.

## Docker and Artifactory

```bash
docker version
```

Expect a working Client and Server, or the approved equivalent. Client-only output plus a daemon
error is not success. The mentor supplies an internal teaching image/digest and safe run recipe
that prints `ONBOARDING_OK` and exits zero. Pull and run it; optionally build/push/pull to a dedicated
teaching namespace if required. Do not pull a public hello-world/base image internally.

Success means the image ran with the expected digest/output. Unauthorized suggests registry access;
manifest unknown suggests path/tag; timeout suggests routing/DNS; TLS needs approved trust;
socket/daemon errors need mentor help. Do not grant broad system privileges as a routine workaround.

## OpenShift teaching workload

Use the internal console or CLI with the mentor. Example read-only checks:

```bash
oc whoami
oc project
oc get pods
oc get svc
oc get routes
```

Expect your identity, the teaching namespace, a Ready workload and known service/route. Inspect
image digest/logs and use the supplied health path, then run the known prediction fixture.
Success requires a request from outside the pod with expected output and loaded artifact ID.
Running or health 200 alone does not establish correct inference.

ImagePullBackOff points toward image/path/pull access; CrashLoopBackOff needs logs; no service
endpoints needs selector/readiness checks; route failures need host/TLS/port checks. The mentor
explains and helps. You need not administer a cluster or memorize status names.

## NFS or PVC persistence

Save a teaching annotation/probe at the approved path and reopen it. With mentor guidance restart
only the teaching workload and read it again. Expect the same record/checksum on persistent storage,
not a temporary container filesystem. This tests persistence, not backup/disaster recovery.
Check mounts, UID/permissions and write path together if it fails. Never restart production for a lab.

## Confluence

Open the approved internal URL, sign in and find the team entry page and a linked working document.
Expect the actual content, not a login redirect or access-denied page. Close and find it again;
identify where service information and owners live. Viewing is enough unless editing is a real
role requirement. DNS/timeouts, SSO loops and page/space permissions are resolved with the mentor.
Internal context stays internal; required learning can be summarized/copied into the internal
course copy when appropriate. Do not export restricted Confluence content to public GitHub.

## GitLab in brief

Create a learning branch, commit a small change and push internally. Open a merge request, choose
source/target and inspect Changes. Follow the pipeline for the same commit and open one safe job
log. Identify the command, result, first relevant error and artifact if present. UI labels vary by
installed version. Retry only a safe teaching job agreed with the mentor, never a production deploy.

Success means you can locate a review and explain the job result. Skipped is not passed; pending
may be runner/queue availability. If this project has no pipeline, use a prepared teaching example.
No requirement to build GitLab CI, manage runners or study YAML. Keep this walkthrough brief.

## Completion checklist

- Internal clone/revision and correct VS Code interpreter/debugger.
- Approved dependency environment and restartable Jupyter kernel.
- Both visualization skills read, installed and activation evidence checked.
- Known code/MCP and Peanuach fixture, with actual output and evidence scope.
- Internal image runs; teaching route returns the expected artifact/output.
- Persistence survives a teaching restart.
- Confluence page can be found and opened; MR/job log can be located.

Complete blocked items with the mentor. A documented access failure is not a research-knowledge
failure, and it is not a pass of an unrun integration check.
