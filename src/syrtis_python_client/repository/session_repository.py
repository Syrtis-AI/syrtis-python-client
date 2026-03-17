from typing import Any

from syrtis_python_client.entity.session import Session
from syrtis_python_client.repository.abstract_api_repository import AbstractApiRepository


class SessionRepository(AbstractApiRepository[Session]):
    @classmethod
    def get_entity_type(cls) -> type[Session]:
        return Session

    def continue_session(
        self,
        session_id: str,
        messages: list[dict[str, Any]],
        *,
        file_stamps: dict[str, Any] | None = None,
        time_zone: str = "UTC",
    ) -> Any:
        return self.client.request_multipart(
            "POST",
            f"session/continue/{session_id}",
            data={
                "messages": messages,
                "fileStamps": file_stamps or {},
                "timeZone": time_zone,
            },
        )

    def continue_session_sync(
        self,
        session_id: str,
        messages: list[dict[str, Any]],
        *,
        file_stamps: dict[str, Any] | None = None,
        time_zone: str = "UTC",
    ) -> Any:
        return self.client.request_multipart(
            "POST",
            f"session/continue/{session_id}/sync",
            data={
                "messages": messages,
                "fileStamps": file_stamps or {},
                "timeZone": time_zone,
            },
        )
