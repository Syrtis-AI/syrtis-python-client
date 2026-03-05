from {{BASE_PACKAGE_NAME}}.entity.abstract_api_entity import AbstractApiEntity


class {{CLASS_NAME}}(AbstractApiEntity):
    @classmethod
    def get_entity_name(cls) -> str:
        return "{{ENTITY_NAME}}"
