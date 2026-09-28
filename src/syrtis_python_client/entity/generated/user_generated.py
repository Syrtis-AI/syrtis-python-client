from sqlalchemy import DateTime, JSON, String
from sqlalchemy.orm import Mapped, declared_attr, mapped_column


class UserGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'user'

    @declared_attr
    def username(cls) -> Mapped[object]:
        return mapped_column(String(180), nullable=False, unique=True)
    @declared_attr
    def secureId(cls) -> Mapped[object]:
        return mapped_column('secure_id', String(255), nullable=False)
    @declared_attr
    def dateCreated(cls) -> Mapped[object]:
        return mapped_column('date_created', DateTime, nullable=False)
    @declared_attr
    def dateLastLogin(cls) -> Mapped[object]:
        return mapped_column('date_last_login', DateTime, nullable=False)
    @declared_attr
    def email(cls) -> Mapped[object]:
        return mapped_column(String(255), nullable=False)
    @declared_attr
    def password(cls) -> Mapped[object]:
        return mapped_column(String, nullable=False)
    @declared_attr
    def firstName(cls) -> Mapped[object]:
        return mapped_column('first_name', String(100), nullable=True)
    @declared_attr
    def lastName(cls) -> Mapped[object]:
        return mapped_column('last_name', String(100), nullable=True)
    @declared_attr
    def roles(cls) -> Mapped[object]:
        return mapped_column(JSON, nullable=False)
