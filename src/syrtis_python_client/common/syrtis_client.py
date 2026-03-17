from __future__ import annotations

from typing import Any
from urllib import parse, request
import json

from syrtis_python_client.common.entity_schemas import get_entity_schemas
from syrtis_python_client.common.generated_repositories import generated_repositories


class SyrtisClient:
    DEFAULT_BASE_URL = "https://api.syrtis.ai/api/"

    def __init__(self, base_url: str | None = None, api_key: str | None = None) -> None:
        self.base_url = (base_url or self.DEFAULT_BASE_URL).rstrip("/") + "/"
        self.api_key = api_key
        self._repositories: dict[type[Any], Any] = {}

    def get_repository_classes(self) -> list[type[Any]]:
        return list(generated_repositories)

    def get_entity_schemas(self) -> dict[str, dict[str, Any]]:
        return get_entity_schemas()

    def get_repository(self, entity_type: type[Any]) -> Any:
        if entity_type in self._repositories:
            return self._repositories[entity_type]

        for repository_class in self.get_repository_classes():
            if repository_class.get_entity_type() is entity_type:
                repository = repository_class(self)
                self._repositories[entity_type] = repository
                return repository

        raise LookupError(
            f"No repository found for entity type: {entity_type.__name__}"
        )

    def request_json(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        payload: dict[str, Any] | None = None,
    ) -> Any:
        url = self.base_url + path.lstrip("/")
        if params:
            url = f"{url}?{parse.urlencode(params, doseq=True)}"

        headers = {"Accept": "application/json"}
        body: bytes | None = None

        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        if payload is not None:
            body = json.dumps(payload).encode("utf-8")
            headers["Content-Type"] = "application/json"

        req = request.Request(
            url=url, method=method.upper(), data=body, headers=headers
        )
        with request.urlopen(req) as response:
            raw = response.read().decode("utf-8")
            if not raw:
                return None
            return json.loads(raw)

    def request_multipart(
        self,
        method: str,
        path: str,
        *,
        data: dict[str, Any],
    ) -> Any:
        url = self.base_url + path.lstrip("/")
        boundary = "----PythonClientBoundary"
        body = (
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="data"\r\n\r\n'
            f"{json.dumps(data)}\r\n"
            f"--{boundary}--\r\n"
        ).encode("utf-8")

        headers = {
            "Accept": "application/json",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        }
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        req = request.Request(
            url=url, method=method.upper(), data=body, headers=headers
        )
        with request.urlopen(req) as response:
            raw = response.read().decode("utf-8")
            if not raw:
                return None
            return json.loads(raw)
