from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.scenario_message_generated import (
    ScenarioMessageGenerated,
)

__all__ = ["ScenarioMessage", "ScenarioMessageGenerated"]


class ScenarioMessage(ScenarioMessageGenerated, AbstractEntity):
    pass
