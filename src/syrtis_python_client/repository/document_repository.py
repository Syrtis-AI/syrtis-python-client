from syrtis_python_client.entity.document import Document
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class DocumentRepository(AbstractApiRepository[Document]):
    @classmethod
    def get_entity_type(cls) -> type[Document]:
        return Document
