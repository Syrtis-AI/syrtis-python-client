from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.environment_generated import (
    EnvironmentGenerated,
)

__all__ = ["Environment", "EnvironmentGenerated"]


class Environment(EnvironmentGenerated, AbstractEntity):
    pass
