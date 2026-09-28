from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.slot_generated import SlotGenerated

__all__ = ["Slot", "SlotGenerated"]


class Slot(SlotGenerated, AbstractEntity):
    TYPE_DEFAULT = "default"
    TYPE_END = "end"
    TYPE_START = "start"

    def get_configs_by_name(self, name: str) -> list:
        return [config for config in self.slotConfigs if config.name == name]

    def is_end(self) -> bool:
        return self.type == self.TYPE_END

    def is_start(self) -> bool:
        return self.type == self.TYPE_START
