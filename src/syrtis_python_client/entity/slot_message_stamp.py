from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.slot_message_stamp_generated import (
    SlotMessageStampGenerated,
)

__all__ = ["SlotMessageStamp", "SlotMessageStampGenerated"]


class SlotMessageStamp(SlotMessageStampGenerated, AbstractEntity):
    pass
