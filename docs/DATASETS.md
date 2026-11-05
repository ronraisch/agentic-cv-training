# Datasets by assignment

The team works on both remote sensing and ordinary-camera video. Satellite/airborne images serve
the imagery assignments. Scene understanding uses ordinary ground, handheld or vehicle cameras;
it is not satellite video. UAV footage below is for the airborne stitching task only.

This is a reference catalog, not another reading course or a requirement to download every source.
Acquire and prepare one small subset per task. Reuse LPR data for evaluation and video data for handover.
Official project/download entry points were checked on 23 October 2026. Archives, annotation files
and internal availability have not been inspected here; suggested subset sizes are planning targets.

| Assignment | Recommended source | Optional alternative or supplement |
|---|---|---|
| 0: setup and Matt Pocock skills | Synthetic fixtures already in the repo; no external ML dataset needed | A tiny approved sample from the later assignments |
| 1: labeling application | [COCO 2017 images and instance annotations](https://cocodataset.org/#download) | [DOTA](https://captain-whu.github.io/DOTA/dataset.html) for remote-sensing examples |
| 2: Hough LPR, then 3: LPR evaluation | [RodoSol-ALPR](https://github.com/raysonlaroca/rodosol-alpr-dataset), or approved Latin/digit plate images | [CCPD](https://github.com/detectRecog/CCPD), with a matching Chinese recognizer |
| 2: stitch two images from a flight | [UAVid, video-supported release](https://uavid.nl/) | An approved team flight with two overlapping frames |
| 3: tracklet motion classification | [UA-DETRAC, author download entry](https://www.albany.edu/faculty/mchang2/chang_download.html) | [VIRAT ground-camera video and tracks](https://viratdata.org/) |
| 3: remote-sensing detection rescoring | [DOTA](https://captain-whu.github.io/DOTA/dataset.html) | [SpaceNet 4 off-nadir buildings](https://spacenet.ai/off-nadir-building-detection/) for an angle-focused variant |
| 4A: cloud segmentation proposal | [CloudSEN12 / CloudSEN12+](https://cloudsen12.github.io/) | Approved team imagery with independent cloud labels |
| 4B: ordinary-camera scene understanding | [MEVA ground-camera subset](https://mevadata.org/) | [BDD100K](https://github.com/bdd100k/bdd100k) driving video or [VIRAT ground-camera subset](https://viratdata.org/) |
| Handover: operational video notebook | The same local Part 4B subset and manifest | New clips from held-out ordinary cameras, not another benchmark |

## Setup and skills

Use deterministic synthetic arrays or existing fixtures for imports, plotting, file roundtrips and
skill activation. Success at setup must not depend on downloading a large dataset. Plotting a
prepared sample later is useful, but does not establish that an internal data mount is accessible.

## Acquire a working subset

Data acquisition is part of the assignment. Follow the source's download/access instructions;
use a small subset rather than the entire benchmark. A request form, account or manual annotation
step is work to plan, not a reason to replace the task with the procedural smoke fixture. If access
cannot be obtained within the assignment's budget, agree another listed source with the mentor.
Inside the closed network, use the owner's approved import procedure; internal connectivity and
transfer paths are supplied separately. Do not try to obtain external data from an isolated pod.

1. Record source URL, release, terms/access status and exact selected source IDs. Request restricted
   data first; do not wait until the exercise is otherwise complete to discover a required form.
2. Download/extract outside Git to `data/imported/<task>/` or the approved storage mount. Keep a
   source inventory with archive/file hashes and extraction commands. Do not flatten conflicting
   filenames from different videos/scenes.
3. Check the exact assets below; labels for a different task are not interchangeable. Decode a
   few images and a video, inspect their annotations and retain their original IDs.
4. Write [an image manifest](COMPONENTS.md#image-manifest) for image inference, or retain source
   video IDs for tracking. Freeze grouped train/validation/test assignments before model fitting.
5. Run [the supplied component command](COMPONENTS.md) on a small subset and inspect its overlays
   or frame records. This establishes that data and frozen inference connect before your change.

| Task | Acquire from source | Local preparation required |
|---|---|---|
| Labeling | COCO download page: `2017 Val images` and `2017 Train/Val annotations` | Select 20-40 image IDs; retain matching `instances_val2017.json` records and convert to [the application bundle](DATA_FORMATS.md) |
| LPR | RodoSol README: request access under its agreement, then obtain images and annotation text; or approved existing Latin/digit imagery | Select about 200-400 images with plate text and corner labels; preserve raw files and source groups. Use supplied Latin OCR. Annotate missing text/corners independently; do not use them as inference inputs |
| Stitching | UAVid download instructions: video-supported release, not only semantic still images | Select two overlapping frames from the same flight, record sequence/frame timestamps; inspect overlap manually |
| Motion | UA-DETRAC author download page: videos plus tracking annotations, or VIRAT ground-camera release | Select 6-10 sequences; run the supplied tracklet producer, or adapt the provided source tracks with provenance. Add independent motion labels; keep whole sequences/cameras together |
| Rescoring | DOTA `images` and `labelTxt` for the same release/partition | Select 50-100 parent images; preserve parent/tile coordinates and annotation polygons. Run frozen vehicle inference, define the target class grouping and HBB conversion for this supplied model; preserve null metadata |
| Clouds | CloudSEN12 project: follow its data/loading example for a pinned release | Select 50-100 patches with suitable dense GT and required bands, retain ROI/date IDs |
| Video | MEVA site: download instructions plus annotation repositories, select ground EO footage | Extract 120-200 ten-second clips with camera/recording/time IDs; add road/indoor/sky labels. Use the existing video baseline and prepared open-model probe |

For CCPD, the source README documents archive access and filename fields for text, box and corner
annotations. Its Chinese province character is outside the supplied OCR alphabet. Use a compatible
recognizer before choosing it for full-plate LPR evaluation. Do not silently evaluate it with Latin OCR.
For RodoSol, retain its annotation text alongside each image; corner order and plate text must be
confirmed from the dataset README and a visual sample. Access approval is not guaranteed.

For the cloud proposal, opening and inspecting an approved small subset is enough; training a
cloud model is not required. For every source, a URL is an acquisition entry point, not a claim
that access or organizational reuse has already been approved.

## Labeling application

COCO supplies ordinary-camera images and instance annotations. Start with about 20-40 images.
Prepare a compatible initial application data bundle; ask product which data to work on.
DOTA offers remote-sensing imagery if the prepared application uses that domain instead.
COCO annotations and individual image rights have different terms; retain the source image-license
information from the [official terms](https://cocodataset.org/#termsofuse).

## Classical CV and LPR evaluation

**LPR:** CCPD includes plate text, axis-aligned boxes and four-corner coordinates encoded in image
filenames, plus challenging subsets such as rotation and tilt. It provides a concrete source for
geometry and recognition experiments. Start with roughly 200-400 mentor-selected images spanning
easy and difficult conditions, subject to what fits the existing budget. Use the same frozen
detector/recognizer and grouped held-out examples for the later paired evaluation. Corner labels
are evaluation references, not an inference input to the proposed Hough method. Filename text is
GT, not a permitted model feature. CCPD's repository declares the dataset MIT-licensed.

RodoSol-ALPR supplies plate text and four corners for Brazilian/Mercosur plates from toll cameras.
It requires a signed academic/noncommercial agreement and an access request; it is not an immediate
download. Its plate layouts differ from CCPD and from Israeli plates. Prepare a compatible frozen
recognizer for the selected source; a recognizer with the wrong alphabet cannot evaluate geometry
fairly. Neither source establishes performance on the team's own camera distribution.

**Stitching:** UAVid provides airborne urban sequences with corresponding videos. Choose two
overlapping frames from the same flight/sequence, a mostly planar region, and enough translation
to create a meaningful larger view. The video-supported release is needed; unrelated labeled stills
are not a guaranteed overlap pair. The mentor must inspect pair suitability and retain timestamps.
Add a small no-overlap or strong-parallax pair as a failure example. UAVid is a segmentation source,
not a stitching benchmark with homography GT: record manual control points/overlap checks separately.
The published license is CC BY-NC-SA 4.0. More than two images remains an approved bonus.

## Evaluation and classical ML

**Tracklets:** UA-DETRAC contains traffic-camera sequences and tracking annotations. Start with
about 6-10 sequences and a few hundred usable tracklets, not the entire benchmark. Run the
[supplied frozen tracker](COMPONENTS.md#tracklets-for-motion-classification), or use a pinned
source export, then define and manually audit a small motion taxonomy with the mentor.
Track IDs and boxes do not automatically supply labels such as turning, stopping or passing.
Keep complete sequences/cameras together in splits; do not randomly split windows of the same
track. Image-plane displacement is not automatically physical speed or object motion under a moving
camera. VIRAT ground video and released tracks are an alternative, subject to its data agreement.
The UA-DETRAC author page links the benchmark; current archive access and reuse terms still need
checking by the person preparing the internal subset.

**Rescoring:** DOTA provides oriented boxes and classes in satellite/aerial imagery. Use roughly
50-100 parent images with independent labels and [frozen detector predictions](COMPONENTS.md#vehicle-predictions-for-rescoring);
include false positives and missed objects. Fit the small rescorer, not another detector. Separate
parent images and overlapping crops across train/validation/test. Inspect GSD availability per image:
missing scale must remain missing. DOTA's small/large-vehicle categories are not bus labels, and its
annotations do not guarantee per-image viewing angles. Do not invent metric dimensions or angle
features. DOTA's published image/annotation terms restrict use to academic purposes.

If viewing angle is the main teaching question, SpaceNet 4 provides multiple off-nadir views and
building footprints. It changes the target from vehicles to buildings and requires a compatible
frozen predictor; choose this variant instead of adding it as another task. Split geographic areas
across all views to prevent seeing the same building on both sides. This source does not validate a
claim about bus dimensions. Use the source's release-specific imagery/label terms.

## Cloud segmentation

CloudSEN12 and its newer CloudSEN12+ collection target Sentinel-2 cloud/cloud-shadow understanding.
Use its official examples to locate data, and pin the exact release and label protocol. The original
collection has dense, scribble and unlabeled groups; only appropriate dense GT should support dense
segmentation evaluation. A proposal can inspect about 50-100 prepared patches without training a
new model. Split by geographic ROI with all related dates grouped. Match the available inference
bands: a multispectral result is not evidence for RGB-only imagery. The original release specifies
CC BY-NC 4.0; inspect the exact selected release's terms before internal packaging. This remains
an eight-hour proposal, not a requirement to transfer the full archive or train on it.

## Ordinary-camera video and handover

**Primary:** MEVA includes ordinary ground-camera footage with indoor/outdoor views. Select only
ground EO/RGB cameras, excluding its separate UAV and thermal sources. Prepare roughly 120-200
ten-second clips across multiple cameras/recordings. Existing activity annotations are useful
references but do not automatically answer this assignment's road/indoor-outdoor/sky-only questions.
Manually label the selected questions and unknown/ambiguous cases. MEVA is published under CC BY 4.0;
its website links download instructions and annotation repositories.

**Optional:** BDD100K provides vehicle-mounted driving video; the official repository links its
dataset resources. Download actual videos, not only the commonly distributed labeled keyframes.
It adds road/driving conditions but does not provide balanced indoor or sky-only negatives.
VIRAT's ground-camera release adds fixed-camera outdoor scenes and events; explicitly exclude
its aerial release and follow its ground-data protection agreement.

Do not make all indoor clips come from one dataset and all outdoor clips from another: a model
could learn source identity. Prefer a single mixed-domain collection plus held-out cameras. If
sky-only or ceiling/empty views are missing, prepare a small approved set of ordinary-camera clips
and annotate them; no listed public dataset is claimed to cover every customer question already.
For any temporal question assigned later, define its time window and audit the labels;
frame annotations are not automatically clip-level event GT. Split at source recording/camera
level and group neighboring or overlapping clips. Reuse these exact assets in the final notebook.

## Closed-network delivery

The source links above remain useful outside the network. The trainee acquires the permitted
subset; the owner handles internal connectivity and approved transfer paths. Inside, use the
transferred bundle or approved storage mount; no runtime access to these sites is assumed. Do not
commit images/videos or whole datasets to Git. The person preparing the data records:

- Source URL, exact release, terms/access status, attribution and selected item IDs.
- Actual file hashes, byte size, paths, decode checks and annotation availability after transfer.
- Frozen split/group manifest, label definitions, missing values and extraction timestamps.
- The approved internal location and a tiny read/decode/annotation smoke check with expected output.

Those fields are preparation requirements, not claims that the data was downloaded, licensed for
this organization or transferred successfully. Check the prepared bundle before beginning an
experiment. Reuse approved internal data if public-source access is unsuitable; ask for help with
unavailable access rather than inventing labels or an alternate unapproved task.

## Embedding VLM and open vocabulary probe

Reuse 12-20 [COCO images/annotations](https://cocodataset.org/#download), a few
[DOTA examples](https://captain-whu.github.io/DOTA/dataset.html) and existing Part 4B
[MEVA ground-camera clips](https://mevadata.org/). No new download/full benchmark is required.
Use annotated object presence/locations to inspect retrieval, localization and VQA outputs;
unannotated categories and arbitrary textual claims still need manual checking. This illustrative
probe cannot establish general accuracy. Keep prompt-development and check examples separate.
