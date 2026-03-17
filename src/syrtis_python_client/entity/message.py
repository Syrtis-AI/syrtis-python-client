from __future__ import annotations

from syrtis_python_client.entity.abstract_api_entity import AbstractApiEntity


class Message(AbstractApiEntity):
    @classmethod
    def get_entity_name(cls) -> str:
        return "message"

    def is_chat_message_from_assistant(self) -> bool:
        return (
            self.data.get("origin") != "user"
            and any(s.get("name") == "chat" for s in self.data.get("messageStamp", []))
        )
