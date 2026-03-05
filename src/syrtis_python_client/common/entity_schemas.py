from __future__ import annotations

from typing import Any

from syrtis_python_client.common.generated_entity_schemas import get_generated_entity_schemas


def get_entity_schemas() -> dict[str, dict[str, Any]]:
    return get_generated_entity_schemas()
