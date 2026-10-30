from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.session_generated import SessionGenerated

__all__ = ["Session", "SessionGenerated"]


class Session(SessionGenerated, AbstractEntity):
    STATUS_COMPLETED = "completed"
    STATUS_OPENED = "opened"

    def get_last_request(self, type: str | None = None):
        requests = [
            request for request in self.requests if type is None or request.type == type
        ]
        return max(requests, key=lambda request: request.id) if requests else None

    def get_previous_request(self, request):
        previous = [other for other in self.requests if other.id < request.id]
        return max(previous, key=lambda other: other.id) if previous else None

    def count_step_requests(self, step, consecutive: bool = False) -> int:
        """Requests made on that step; `consecutive` counts back from the latest
        request and stops at the first one made on another step."""
        count = 0
        for request in sorted(self.requests, key=lambda request: request.id, reverse=True):
            if request.step is step:
                count += 1
            elif consecutive:
                break
        return count
