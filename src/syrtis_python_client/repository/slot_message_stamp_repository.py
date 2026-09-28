from syrtis_python_client.entity.slot_message_stamp import SlotMessageStamp
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class SlotMessageStampRepository(AbstractApiRepository[SlotMessageStamp]):
    @classmethod
    def get_entity_type(cls) -> type[SlotMessageStamp]:
        return SlotMessageStamp
