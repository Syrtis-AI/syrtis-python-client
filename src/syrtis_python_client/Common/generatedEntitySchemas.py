from __future__ import annotations

import json
from importlib.resources import files
from typing import Any


def get_generated_entity_schemas() -> dict[str, dict[str, Any]]:
    schema_file = files("syrtis_python_client.data.entity").joinpath("uesr.json")
    schema = json.loads(schema_file.read_text(encoding="utf-8"))
    return {schema["name"]: schema}
