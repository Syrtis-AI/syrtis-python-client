from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class DocumentGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'document'

    @declared_attr
    def dateCreated(cls) -> Mapped[object]:
        return mapped_column('date_created', DateTime, nullable=False)
    @declared_attr
    def title(cls) -> Mapped[object]:
        return mapped_column(String(255), nullable=False)
    @declared_attr
    def secureId(cls) -> Mapped[object]:
        return mapped_column('secure_id', String(255), nullable=False)
    @declared_attr
    def mimeType(cls) -> Mapped[object]:
        return mapped_column('mime_type', String(255), nullable=False)
    @declared_attr
    def type(cls) -> Mapped[object]:
        return mapped_column(String(120), nullable=False)
    @declared_attr
    def content(cls) -> Mapped[object]:
        return mapped_column(Text, nullable=True)

    @declared_attr
    def user_id(cls) -> Mapped[object]:
        return mapped_column(Integer, ForeignKey('user.id'), nullable=False)
    @declared_attr
    def user(cls) -> Mapped[object]:
        return relationship('User', foreign_keys='Document.user_id', lazy='select')
    @declared_attr
    def project_id(cls) -> Mapped[object]:
        return mapped_column(Integer, nullable=False)
