from syrtis_python_client.entity.card_message import CardMessage
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class CardMessageRepository(AbstractApiRepository[CardMessage]):
    @classmethod
    def get_entity_type(cls) -> type[CardMessage]:
        return CardMessage
