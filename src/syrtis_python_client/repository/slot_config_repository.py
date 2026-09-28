from syrtis_python_client.entity.slot_config import SlotConfig
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class SlotConfigRepository(AbstractApiRepository[SlotConfig]):
    @classmethod
    def get_entity_type(cls) -> type[SlotConfig]:
        return SlotConfig
