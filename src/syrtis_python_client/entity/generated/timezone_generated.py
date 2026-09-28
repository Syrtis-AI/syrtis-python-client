from sqlalchemy import String
from sqlalchemy.orm import Mapped, declared_attr, mapped_column


class TimezoneGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'timezone'

    @declared_attr
    def name(cls) -> Mapped[object]:
        return mapped_column(String(255), nullable=False)
