from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.step_message_generated import (
    StepMessageGenerated,
)

__all__ = ["StepMessage", "StepMessageGenerated"]


class StepMessage(StepMessageGenerated, AbstractEntity):
    pass
