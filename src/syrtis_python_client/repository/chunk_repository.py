from syrtis_python_client.entity.chunk import Chunk
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class ChunkRepository(AbstractApiRepository[Chunk]):
    @classmethod
    def get_entity_type(cls) -> type[Chunk]:
        return Chunk
