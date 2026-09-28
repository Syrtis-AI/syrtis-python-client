#!/usr/bin/env python3
"""Generate the entities of this client from its registry schemas
(`data/entity/*.json`): SQLAlchemy classes through wexample_orm, and the
schema manifest read by `SyrtisClient.get_entity_schemas()`.

The internal client also sees the public one's entities, and gets the
database repositories of both."""

from __future__ import annotations

from pathlib import Path

PUBLIC_PACKAGE_NAME = "syrtis_python_client"


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
    from wexample_orm.generator.entity_generator import EntityGenerator
    from wexample_orm.generator.repository_generator import RepositoryGenerator

    src_dir = Path(__file__).resolve().parent.parent / "src"
    [package_dir] = [
        path for path in src_dir.iterdir() if path.name.startswith(PUBLIC_PACKAGE_NAME)
    ]
    package_name = package_dir.name
    is_internal = package_name != PUBLIC_PACKAGE_NAME

    counts = EntityGenerator(
        external_package_name=PUBLIC_PACKAGE_NAME if is_internal else None,
        package_dir=package_dir,
        package_name=package_name,
    ).generate()
    print(f"Entities: {counts}")

    if is_internal:
        counts = RepositoryGenerator(
            entity_package_names=[PUBLIC_PACKAGE_NAME, package_name],
            package_dir=package_dir,
            package_name=package_name,
        ).generate()
        print(f"Database repositories: {counts}")

    json_files = sorted(path.name for path in (package_dir / "data" / "entity").glob("*.json"))
    (package_dir / "common" / "generated_entity_schemas.py").write_text(
        build_schema_manifest(package_name, json_files), encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
