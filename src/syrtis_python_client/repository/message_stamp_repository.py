from syrtis_python_client.entity.message_stamp import MessageStamp
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class MessageStampRepository(AbstractApiRepository[MessageStamp]):
    @classmethod
    def get_entity_type(cls) -> type[MessageStamp]:
        return MessageStamp
