#!/usr/bin/env python3
from __future__ import annotations

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


def build_repositories_manifest(package_name: str, repo_modules: list[str]) -> str:
    imports = "\n".join(
        f"from {package_name}.repository.{module} import {to_pascal_case(module[:-11])}Repository"
        for module in repo_modules
    )
    classes = "\n".join(
        f"    {to_pascal_case(module[:-11])}Repository," for module in repo_modules
    )

    return f'''{imports}


generated_repositories = [
{classes}
]
'''


def main() -> int:
    root_dir = Path(__file__).resolve().parent.parent
    src_dir = root_dir / "src"
    package_name = detect_package_name(src_dir)
    package_dir = src_dir / package_name
    data_dir = package_dir / "data" / "entity"
    repository_dir = package_dir / "repository"
    common_dir = package_dir / "common"
    template_path = root_dir / "bin" / "template" / "repository.py.tpl"

    if not data_dir.is_dir():
        print(f"Error: missing data directory: {data_dir}", file=sys.stderr)
        return 1

    repository_dir.mkdir(parents=True, exist_ok=True)
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

        repository_module_name = f"{module_name}_repository"
        target_path = repository_dir / f"{repository_module_name}.py"

        if target_path.exists():
            skipped += 1
            continue

        content = (
            template.replace("{{PACKAGE_NAME}}", package_name)
            .replace("{{CLASS_NAME}}", class_name)
            .replace("{{ENTITY_MODULE_NAME}}", module_name)
        )
        target_path.write_text(content, encoding="utf-8")
        created += 1
        print(f"Created {target_path}")

    repository_modules = sorted(
        path.stem
        for path in repository_dir.iterdir()
        if path.suffix == ".py"
        and path.stem.endswith("_repository")
        and path.stem != "abstract_api_repository"
    )

    manifest_path = common_dir / "generated_repositories.py"
    manifest_content = build_repositories_manifest(package_name, repository_modules)
    manifest_path.write_text(manifest_content, encoding="utf-8")
    print(f"Updated {manifest_path}")

    print(f"Done: created={created}, skipped={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
