from syrtis_python_client.entity.node import Node
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class NodeRepository(AbstractApiRepository[Node]):
    @classmethod
    def get_entity_type(cls) -> type[Node]:
        return Node
