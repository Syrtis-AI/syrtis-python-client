from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.message_stamp_generated import (
    MessageStampGenerated,
)

__all__ = ["MessageStamp", "MessageStampGenerated"]


class MessageStamp(MessageStampGenerated, AbstractEntity):
    pass
