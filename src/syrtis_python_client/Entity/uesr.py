from syrtis_python_client.Entity.abstract_api_entity import AbstractApiEntity


class Uesr(AbstractApiEntity):
    @classmethod
    def get_entity_name(cls) -> str:
        return "uesr"
