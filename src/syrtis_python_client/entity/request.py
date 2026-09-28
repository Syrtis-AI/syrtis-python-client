from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.request_generated import RequestGenerated

__all__ = ["Request", "RequestGenerated"]


class Request(RequestGenerated, AbstractEntity):
    STATUS_COMPLETE = "complete"
    STATUS_ERROR = "error"
    STATUS_PENDING = "pending"
    STATUS_PROCESSING = "processing"

    TYPE_CASCADE = "cascade"
    TYPE_SCHEDULE = "schedule"
    TYPE_USER = "user"

    def get_branch(self) -> list:
        """This request and its ancestors, the most recent first."""
        branch = []
        request = self
        while request is not None:
            branch.append(request)
            request = request.parent
        return branch
