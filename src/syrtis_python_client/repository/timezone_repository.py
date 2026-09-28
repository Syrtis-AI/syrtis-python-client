from syrtis_python_client.entity.timezone import Timezone
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class TimezoneRepository(AbstractApiRepository[Timezone]):
    @classmethod
    def get_entity_type(cls) -> type[Timezone]:
        return Timezone
