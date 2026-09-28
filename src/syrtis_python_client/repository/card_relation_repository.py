from syrtis_python_client.entity.card_relation import CardRelation
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class CardRelationRepository(AbstractApiRepository[CardRelation]):
    @classmethod
    def get_entity_type(cls) -> type[CardRelation]:
        return CardRelation
