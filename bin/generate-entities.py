#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def to_pascal_case(value: str) -> str:
    parts = [part for part in re.split(r"[^a-zA-Z0-9]+", value.strip()) if part]
    return "".join(part[:1].upper() + part[1:] for part in parts)


def to_snake_case(value: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "_", value.strip()).strip("_").lower()
    return re.sub(r"_+", "_", cleaned)


def detect_package_name(src_dir: Path) -> str:
    candidates = sorted(
        item.name
        for item in src_dir.iterdir()
        if item.is_dir() and item.name.startswith("syrtis_python_client")
    )
    if len(candidates) != 1:
        raise RuntimeError(
            f"Unable to detect package under {src_dir}: found {candidates}"
        )
    return candidates[0]


def build_schema_manifest(package_name: str, json_files: list[str]) -> str:
    file_entries = "\n".join(f'    "{name}",' for name in json_files)
    return f'''from __future__ import annotations

import json
from importlib.resources import files
from typing import Any

ENTITY_SCHEMA_FILES = [
{file_entries}
]


def get_generated_entity_schemas() -> dict[str, dict[str, Any]]:
    data_package = "{package_name}.data.entity"
    schemas: dict[str, dict[str, Any]] = {{}}

    for file_name in ENTITY_SCHEMA_FILES:
        schema_file = files(data_package).joinpath(file_name)
        schema = json.loads(schema_file.read_text(encoding="utf-8"))
        schemas[schema["name"]] = schema

    return schemas
'''


def main() -> int:
    root_dir = Path(__file__).resolve().parent.parent
    src_dir = root_dir / "src"
    package_name = detect_package_name(src_dir)
    package_dir = src_dir / package_name
    data_dir = package_dir / "data" / "entity"
    entity_dir = package_dir / "entity"
    common_dir = package_dir / "common"
    template_path = root_dir / "bin" / "template" / "entity.py.tpl"

    if not data_dir.is_dir():
        print(f"Error: missing data directory: {data_dir}", file=sys.stderr)
        return 1

    entity_dir.mkdir(parents=True, exist_ok=True)
    common_dir.mkdir(parents=True, exist_ok=True)

    if not template_path.is_file():
        print(f"Error: missing template file: {template_path}", file=sys.stderr)
        return 1

    template = template_path.read_text(encoding="utf-8")
    json_files = sorted(path for path in data_dir.iterdir() if path.suffix == ".json")

    created = 0
    skipped = 0

    for file_path in json_files:
        entity_name = file_path.stem
        class_name = to_pascal_case(entity_name)
        module_name = to_snake_case(entity_name)

        if not class_name or not module_name or class_name == "AbstractApiEntity":
            skipped += 1
            continue

        target_path = entity_dir / f"{module_name}.py"
        if target_path.exists():
            skipped += 1
            continue

        content = (
            template.replace("{{PACKAGE_NAME}}", package_name)
            .replace("{{CLASS_NAME}}", class_name)
            .replace("{{ENTITY_NAME}}", entity_name)
        )
        target_path.write_text(content, encoding="utf-8")
        created += 1
        print(f"Created {target_path}")

    manifest_path = common_dir / "generated_entity_schemas.py"
    manifest_content = build_schema_manifest(
        package_name=package_name,
        json_files=[path.name for path in json_files],
    )
    manifest_path.write_text(manifest_content, encoding="utf-8")
    print(f"Updated {manifest_path}")

    print(f"Done: created={created}, skipped={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
