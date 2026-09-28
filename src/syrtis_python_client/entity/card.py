from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.card_generated import CardGenerated

__all__ = ["Card", "CardGenerated"]


class Card(CardGenerated, AbstractEntity):
    SCOPE_DEFAULT = "default"
    SCOPE_GLOBAL = "global"

    def get_messages(self) -> list:
        return [card_message.message for card_message in self.cardMessages]

    def get_next_cards(self) -> list:
        """Targets of the relations leaving this card, in relation order."""
        return [
            relation.cardTarget
            for relation in sorted(self.cardRelationsSources, key=lambda relation: relation.id)
        ]

    def get_previous_cards(self) -> list:
        """Sources of the relations reaching this card, in relation order."""
        return [
            relation.cardSource
            for relation in sorted(self.cardRelationsTarget, key=lambda relation: relation.id)
        ]
