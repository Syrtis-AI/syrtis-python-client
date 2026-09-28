from syrtis_python_client.entity.environment import Environment
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class EnvironmentRepository(AbstractApiRepository[Environment]):
    @classmethod
    def get_entity_type(cls) -> type[Environment]:
        return Environment
