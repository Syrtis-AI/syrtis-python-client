from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.step_generated import (
    StepGenerated,
)

__all__ = ["Step", "StepGenerated"]


class Step(StepGenerated, AbstractEntity):
    pass
