from __future__ import annotations

from typing import Any, Generic, TypeVar

from syrtis_python_client.entity.abstract_api_entity import AbstractApiEntity

EntityType = TypeVar("EntityType", bound=AbstractApiEntity)


class AbstractApiRepository(Generic[EntityType]):
    def __init__(self, client: Any) -> None:
        self.client = client

    @classmethod
    def get_entity_type(cls) -> type[EntityType]:
        raise NotImplementedError

    def _entity_path(self) -> str:
        entity_type = self.get_entity_type()
        return entity_type.get_entity_name()

    def list(self, params: dict[str, Any] | None = None) -> Any:
        return self.client.request_json("GET", self._entity_path(), params=params)

    def get(self, item_id: str | int) -> Any:
        return self.client.request_json("GET", f"{self._entity_path()}/{item_id}")

    def create(self, payload: dict[str, Any]) -> Any:
        return self.client.request_json("POST", self._entity_path(), payload=payload)

    def update(self, item_id: str | int, payload: dict[str, Any]) -> Any:
        return self.client.request_json(
            "PUT", f"{self._entity_path()}/{item_id}", payload=payload
        )

    def delete(self, item_id: str | int) -> Any:
        return self.client.request_json("DELETE", f"{self._entity_path()}/{item_id}")
