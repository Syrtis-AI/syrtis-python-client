from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.card_message_generated import (
    CardMessageGenerated,
)

__all__ = ["CardMessage", "CardMessageGenerated"]


class CardMessage(CardMessageGenerated, AbstractEntity):
    pass
