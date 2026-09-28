from syrtis_python_client.entity.slot_relation import SlotRelation
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class SlotRelationRepository(AbstractApiRepository[SlotRelation]):
    @classmethod
    def get_entity_type(cls) -> type[SlotRelation]:
        return SlotRelation
