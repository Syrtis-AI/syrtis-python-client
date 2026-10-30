from syrtis_python_client.entity.scenario_message import ScenarioMessage
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class ScenarioMessageRepository(AbstractApiRepository[ScenarioMessage]):
    @classmethod
    def get_entity_type(cls) -> type[ScenarioMessage]:
        return ScenarioMessage
