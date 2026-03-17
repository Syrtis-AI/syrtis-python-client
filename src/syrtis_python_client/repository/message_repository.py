from __future__ import annotations

from syrtis_python_client.entity.message import Message
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class MessageRepository(AbstractApiRepository[Message]):
    @classmethod
    def get_entity_type(cls) -> type[Message]:
        return Message
