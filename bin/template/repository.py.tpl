from {{PACKAGE_NAME}}.entity.{{ENTITY_MODULE_NAME}} import {{CLASS_NAME}}
from {{PACKAGE_NAME}}.repository.abstract_api_repository import AbstractApiRepository


class {{CLASS_NAME}}Repository(AbstractApiRepository[{{CLASS_NAME}}]):
    @classmethod
    def get_entity_type(cls) -> type[{{CLASS_NAME}}]:
        return {{CLASS_NAME}}
