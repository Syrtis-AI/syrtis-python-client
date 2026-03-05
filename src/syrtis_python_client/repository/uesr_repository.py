from syrtis_python_client.entity.uesr import Uesr
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class UesrRepository(AbstractApiRepository[Uesr]):
    @classmethod
    def get_entity_type(cls) -> type[Uesr]:
        return Uesr
