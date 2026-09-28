from syrtis_python_client.entity.scenario import Scenario
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class ScenarioRepository(AbstractApiRepository[Scenario]):
    @classmethod
    def get_entity_type(cls) -> type[Scenario]:
        return Scenario
