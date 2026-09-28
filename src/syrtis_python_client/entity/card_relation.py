from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.card_relation_generated import (
    CardRelationGenerated,
)

__all__ = ["CardRelation", "CardRelationGenerated"]


class CardRelation(CardRelationGenerated, AbstractEntity):
    pass
