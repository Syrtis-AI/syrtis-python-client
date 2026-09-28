from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.slot_relation_generated import (
    SlotRelationGenerated,
)

__all__ = ["SlotRelation", "SlotRelationGenerated"]


class SlotRelation(SlotRelationGenerated, AbstractEntity):
    pass
