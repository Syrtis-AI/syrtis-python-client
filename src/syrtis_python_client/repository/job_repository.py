from syrtis_python_client.entity.job import Job
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class JobRepository(AbstractApiRepository[Job]):
    @classmethod
    def get_entity_type(cls) -> type[Job]:
        return Job
