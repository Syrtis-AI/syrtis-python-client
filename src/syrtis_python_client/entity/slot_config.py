from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.slot_config_generated import (
    SlotConfigGenerated,
)

__all__ = ["SlotConfig", "SlotConfigGenerated"]


class SlotConfig(SlotConfigGenerated, AbstractEntity):
    pass
