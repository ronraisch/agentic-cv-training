# Stage 0 Visualization skills

This lab treats Matplotlib literally as the plotting tool named in the request. It is separate
from the previously discussed Matt Pocock engineering-skill collection. Do not silently install
a large unrelated skill pack. The required pair is `matplotlib` and `scientific-visualization` from
K-Dense-AI/scientific-agent-skills, pinned at commit
`593377bb048752abb0152deab9fbb1083a6087df`.

| Skill | Main responsibility | Example trigger |
|---|---|---|
| matplotlib | Implement/debug plot elements, axes, layouts and static exports | Correctly label and export a PR plot |
| scientific-visualization | Review figure meaning, comparability, uncertainty, accessibility and delivery | Compare model results without misleading scales or missing-data treatment |

They can work together. A skill is instructions/workflow, not the Matplotlib Python package, a
permission grant or an independent evaluation of the science. Do not load every reference body
for a tiny chart. Read the entry instructions and only the relevant reference sections.

## Offline installation exercise

The mentor prepares an approved source snapshot at the pinned commit, with both complete skill
directories, their references/scripts/assets, licenses and a checksum inventory. Snapshot directory
trees: matplotlib `5878841efa26086ca904f5532fe057fdb20885e1`;
scientific-visualization `292eaa2adb46c1ee678f090efec7780c50b91419`.
These are upstream Git tree IDs, not SHA256 checksums or proof of local installation.

1. Verify the approved snapshot revision and its file inventory with the mentor.
2. Install both complete directories into the approved client's project skill location. For this
   course `.agents/skills/<name>/SKILL.md` is the portable source location, not a promise that every
   client discovers it automatically. Configure the actual client or explicitly supply the path.
3. Read the two SKILL.md entry files. Explain roles/triggers, dependencies and what they cannot prove.
4. Confirm the Python environment already has approved plotting dependencies from Artifactory.
   Do not run upstream public `uv add`/isolated-download examples blindly or overwrite project pins.
5. In a fresh approved agent session request one small plot on synthetic values. Record the loaded
   skill trace, actual output and a case that should not load visualization skills, such as renaming
   an API field. Merely copying a directory is not activation evidence.
6. Export a PNG in a headless environment and inspect labels/units. Use the approved environment;
   no GUI, cloud account or external credentials are needed for static output.

Example copy commands after the mentor supplies a complete approved snapshot:

```bash
# Replace the path with the approved internal snapshot, not a public download.
TEAM_SKILL_SNAPSHOT=/approved/path/scientific-agent-skills
# Inspect revision and ensure destinations do not already exist before copying.
git -C "$TEAM_SKILL_SNAPSHOT" rev-parse HEAD
mkdir -p .agents/skills
cp -R "$TEAM_SKILL_SNAPSHOT/skills/matplotlib" .agents/skills/matplotlib
cp -R "$TEAM_SKILL_SNAPSHOT/skills/scientific-visualization" .agents/skills/scientific-visualization
```

Do not overwrite an existing installed skill; compare revision and agree an update first. Preserve
upstream license files in the approved bundle. Installing the source skill does not install its
Python dependencies. For file-only plotting, a local Agg backend avoids a display requirement;
Jupyter widgets need a separate working backend and are not required for this check.

## Preparation and teach-back

Within the six-hour guided-setup allocation, allow about 75 minutes for installation, reading and
the small activation experiment. The mentor attends a 30-minute check inside the week-1 meeting:
5 minutes roles; 10 explain a synthetic plot and the relevant skill; 10 challenge a misleading
comparison/uncertainty claim; 5 negative trigger and offline dependencies. No extra daily meeting.
Record source revision, loaded trace, output, version limitations and remaining blocked checks.

This repository supplies the exercise, source pin and installation instructions. It does not claim
that these upstream skills have already been installed or activated in the team's internal client.
