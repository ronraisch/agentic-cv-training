"""Local labeled image collections shared by the annotation app and detector."""

from functools import partial
import json
from pathlib import Path
import sqlite3

from researchlab import demo


DOMAINS = ("coco", "video", "drone", "satellite")
SPLITS = ("train", "validation", "test")


def load_collection(root, domain):
    root = Path(root) / domain
    if not (root / "manifest.json").is_file():
        raise demo.missing("labeling dataset manifest", root / "manifest.json",
                           "Mount the prepared dataset. See docs/DATA_FORMATS.md#labeling-collections.")
    manifest = demo.load_manifest(root)
    source = manifest.get("source")
    if (not isinstance(source, str) or not source.strip()
            or source.lower().startswith(("procedural", "synthetic")) or manifest.get("domain") != domain):
        raise demo.DemoError(f"{root}/manifest.json: expected a real {domain} collection with source provenance")
    samples = {}
    classes = manifest.get("classes")
    if (not isinstance(classes, list) or not classes or
            not all(isinstance(name, str) and name.strip() for name in classes)
            or len(set(classes)) != len(classes)):
        raise demo.DemoError(f"{root}/manifest.json: expected unique class names in classes")
    validate = partial(demo.validate_annotations, classes=classes)
    hashes = {}
    for sample in manifest["samples"]:
        path = root / sample["path"]
        try:
            if sample["kind"] != "image":
                raise demo.DemoError("Expected individual labeled RGB frames/images")
            if not all(isinstance(sample[field], str) and sample[field].strip()
                       for field in ("id", "group_id")):
                raise demo.DemoError("Expected nonempty image and source-group IDs")
            if hashes.setdefault(sample["sha256"], sample["split"]) != sample["split"]:
                raise demo.DemoError("Identical image bytes appear in more than one source split")
            if domain == "video":
                timestamp = sample.get("timestamp_seconds")
                if type(timestamp) not in (int, float) or not 0 <= timestamp < float("inf"):
                    raise demo.DemoError("Expected a nonnegative timestamp_seconds for the source frame")
            height, width = demo.pixels(root, sample).shape[:2]
            validate({"schema_version": 1, "annotations": sample["annotations"]}, width, height)
            samples[sample["id"]] = sample
        except (KeyError, ValueError, OSError, TypeError) as error:
            raise demo.DemoError(f"{path}: {error}. See docs/DATA_FORMATS.md#labeling-collections") from error
    if not any(sample["annotations"] for sample in samples.values()):
        raise demo.DemoError(f"{root}/manifest.json: expected at least one annotated object")
    return root, manifest, samples


def load_labeling(root):
    collections, errors = {}, []
    for domain in DOMAINS:
        try:
            collections[domain] = load_collection(root, domain)
        except (demo.DemoError, OSError) as error:
            errors.append(f"{domain}: {error}")
    if errors:
        raise demo.DemoError("Cannot open the labeling datasets:\n" + "\n".join(errors))
    for path, manifest, samples in collections.values():
        try:
            demo.initialize_store(path, manifest)
            snapshot = demo.annotation_snapshot(path)
            for image_id, sample in samples.items():
                record = snapshot[image_id]
                if record["image_id"] != image_id:
                    raise demo.DemoError(f"Record for {image_id} has the wrong image_id")
                height, width = demo.pixels(path, sample).shape[:2]
                demo.validate_annotations(record, width, height, manifest["classes"])
        except (sqlite3.Error, KeyError, ValueError, TypeError, OSError) as error:
            raise demo.DemoError(f"{path}/labels.sqlite: {error}. See docs/DATA_FORMATS.md") from error
    return collections


def write_manifest(root, domain, source, classes, samples):
    """Write an index for pre-staged source images or extracted video frames."""
    root = Path(root)
    destination = root / "manifest.json"
    if destination.exists():
        raise demo.DemoError(f"{destination} already exists; use a fresh collection directory")
    for sample in samples:
        sample["kind"] = "image"
        sample["sha256"] = demo.digest(demo.asset_path(root, sample["path"]))
    manifest = {"schema_version": 1, "domain": domain, "source": source,
                "classes": classes, "samples": samples}
    with destination.open("x") as stream:
        try:
            json.dump(manifest, stream, indent=2)
            stream.flush()
            _, _, loaded = load_collection(root.parent, domain)
        except (ValueError, OSError, TypeError, KeyError):
            destination.unlink()
            raise
    return loaded
