from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class AbstractApiEntity:
    """Base entity storing raw API payload."""

    data: dict[str, Any]

    @classmethod
    def from_payload(cls, payload: dict[str, Any]) -> AbstractApiEntity:
        return cls(data=payload)

    @classmethod
    def get_entity_name(cls) -> str:
        name = cls.__name__
        if name.startswith("Abstract"):
            return ""
        return name.lower()

    def to_dict(self) -> dict[str, Any]:
        return dict(self.data)
