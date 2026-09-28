from syrtis_python_client.entity.template import Template
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class TemplateRepository(AbstractApiRepository[Template]):
    @classmethod
    def get_entity_type(cls) -> type[Template]:
        return Template
