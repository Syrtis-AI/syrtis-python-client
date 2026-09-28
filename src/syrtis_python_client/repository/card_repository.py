from syrtis_python_client.entity.card import Card
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class CardRepository(AbstractApiRepository[Card]):
    @classmethod
    def get_entity_type(cls) -> type[Card]:
        return Card
