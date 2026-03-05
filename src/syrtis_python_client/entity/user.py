from syrtis_python_client.entity.abstract_api_entity import AbstractApiEntity


class User(AbstractApiEntity):
    @classmethod
    def get_entity_name(cls) -> str:
        return "user"
