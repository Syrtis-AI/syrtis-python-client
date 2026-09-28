from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.slot_message_generated import SlotMessageGenerated

__all__ = ["SlotMessage", "SlotMessageGenerated"]


class SlotMessage(SlotMessageGenerated, AbstractEntity):
    COLLECTION_DEBUG = "debug"
    COLLECTION_DEFAULT = "default"
    COLLECTION_ERROR = "error"
    COLLECTION_SAY = "say"
    COLLECTION_TOOL = "tool"
    COLLECTION_WARNING = "warning"

    DIRECTION_INPUT = "input"
    DIRECTION_OUTPUT = "output"

    SOURCE_CARD = "card"
    SOURCE_FULL_HISTORY = "full-history"
    SOURCE_GLOBAL_CARD = "global-card"
    SOURCE_HISTORY = "history"
    SOURCE_MESSAGES_BAG = "messages-bag"
    SOURCE_NODE = "node"
    SOURCE_PREVIOUS_REQUEST = "previous-request"
    SOURCE_REQUEST = "request"

    TYPE_SELECTOR = "selector"
    TYPE_SPECIFIC = "specific"

    def get_stamps_names(self) -> list[str]:
        return [stamp.name for stamp in self.slotMessageStamps]

    def matches(self, message) -> bool:
        """Whether a message passes this selector's name, format, content type
        and stamps filters."""
        if self.name and message.name != self.name:
            return False
        if self.format and message.format != self.format:
            return False
        if self.contentType and message.contentType != self.contentType:
            return False
        return message.has_stamps_name(self.get_stamps_names())
