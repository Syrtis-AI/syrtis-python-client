from syrtis_python_client.entity.step_message import StepMessage
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class StepMessageRepository(AbstractApiRepository[StepMessage]):
    @classmethod
    def get_entity_type(cls) -> type[StepMessage]:
        return StepMessage
