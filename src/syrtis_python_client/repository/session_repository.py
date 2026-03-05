from syrtis_python_client.entity.session import Session
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class SessionRepository(AbstractApiRepository[Session]):
    @classmethod
    def get_entity_type(cls) -> type[Session]:
        return Session
