from __future__ import annotations

import json
from importlib.resources import files
from typing import Any

ENTITY_SCHEMA_FILES = [
    "uesr.json",
]


def get_generated_entity_schemas() -> dict[str, dict[str, Any]]:
    data_package = "syrtis_python_client.data.entity"
    schemas: dict[str, dict[str, Any]] = {}

    for file_name in ENTITY_SCHEMA_FILES:
        schema_file = files(data_package).joinpath(file_name)
        schema = json.loads(schema_file.read_text(encoding="utf-8"))
        schemas[schema["name"]] = schema

    return schemas
