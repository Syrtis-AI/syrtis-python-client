from syrtis_python_client.entity.slot import Slot
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class SlotRepository(AbstractApiRepository[Slot]):
    @classmethod
    def get_entity_type(cls) -> type[Slot]:
        return Slot
