from syrtis_python_client.entity.slot_message import SlotMessage
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class SlotMessageRepository(AbstractApiRepository[SlotMessage]):
    @classmethod
    def get_entity_type(cls) -> type[SlotMessage]:
        return SlotMessage
