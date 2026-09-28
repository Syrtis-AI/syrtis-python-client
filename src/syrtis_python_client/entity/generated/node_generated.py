from sqlalchemy import String
from sqlalchemy.orm import Mapped, declared_attr, mapped_column


class NodeGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'node'

    @declared_attr
    def type(cls) -> Mapped[object]:
        return mapped_column(String(120), nullable=False)
    @declared_attr
    def secureId(cls) -> Mapped[object]:
        return mapped_column('secure_id', String(255), nullable=False)
