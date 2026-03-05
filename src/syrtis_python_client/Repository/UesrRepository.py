from syrtis_python_client.Entity.Uesr import Uesr
from syrtis_python_client.Repository.AbstractApiRepository import AbstractApiRepository


class UesrRepository(AbstractApiRepository[Uesr]):
    @classmethod
    def get_entity_type(cls) -> type[Uesr]:
        return Uesr
