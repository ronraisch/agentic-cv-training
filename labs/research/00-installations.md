# Stage 0 Guided setup

Follow [internal setup](../../docs/GETTING_STARTED_INTERNAL.md) with the mentor.
Obtain VS Code, OpenShift, GitLab, Artifactory, Confluence and Jupyter access using the existing stack.
First install VS Code and connect it to your own OpenShift development pod. Then install/configure
OMP there with the approved local LLM service (currently QWEN 3.8), following
[the OMP readiness checks](../../docs/GETTING_STARTED_INTERNAL.md#omp-and-the-local-llm).
Verify an actual model request, workspace tool use and reconnect before skill activation.
For each check record the expected output, actual output, evidence scope and owner if blocked.

Complete [the Matt Pocock skill lab](../../docs/SKILLS_STAGE0.md): install the approved Matt Pocock skill bundle, skim the catalog descriptions and follow the selected
deep-practice list. Explain when each workflow fits.
Use a successful activation trace and a case that should not trigger them. Installing a Python
package is not the same as installing a skill. The 30-minute teach-back is inside week 1's budget.

Show a correct interpreter, notebook restart, internal fixture request, Confluence page and safe
GitLab job log. Infrastructure is guided learning, not a DevOps assessment. Do not reinstall the
team's entire stack or fetch public packages from the closed network.

[Relevant data sources](../../docs/DATASETS.md#setup-and-skills). Use the mentor-prepared internal subset.
