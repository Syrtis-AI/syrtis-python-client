from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.user_generated import (
    UserGenerated,
)

__all__ = ["User", "UserGenerated"]


class User(UserGenerated, AbstractEntity):
    pass
