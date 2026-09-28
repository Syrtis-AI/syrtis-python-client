from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.timezone_generated import (
    TimezoneGenerated,
)

__all__ = ["Timezone", "TimezoneGenerated"]


class Timezone(TimezoneGenerated, AbstractEntity):
    pass
