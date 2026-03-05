from syrtis_python_client.Entity.AbstractApiEntity import AbstractApiEntity


class Uesr(AbstractApiEntity):
    @classmethod
    def get_entity_name(cls) -> str:
        return "uesr"
