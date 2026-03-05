from syrtis_python_client.entity.request import Request
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class RequestRepository(AbstractApiRepository[Request]):
    @classmethod
    def get_entity_type(cls) -> type[Request]:
        return Request
