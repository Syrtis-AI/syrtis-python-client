from syrtis_python_client.entity.step import Step
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class StepRepository(AbstractApiRepository[Step]):
    @classmethod
    def get_entity_type(cls) -> type[Step]:
        return Step
