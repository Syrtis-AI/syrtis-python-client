from syrtis_python_client.entity.user import User
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class UserRepository(AbstractApiRepository[User]):
    @classmethod
    def get_entity_type(cls) -> type[User]:
        return User
