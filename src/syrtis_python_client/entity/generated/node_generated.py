from sqlalchemy import String
from sqlalchemy.orm import Mapped, declared_attr, mapped_column


class NodeGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'node'

    @declared_attr
    def type(cls) -> Mapped[object]:
        return mapped_column(String(120), nullable=False)
