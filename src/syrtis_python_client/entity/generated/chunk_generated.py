from sqlalchemy import DateTime, ForeignKey, Text, Uuid
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class ChunkGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'chunk'

    @declared_attr
    def content(cls) -> Mapped[object]:
        return mapped_column(Text, nullable=True)
    @declared_attr
    def dateCreated(cls) -> Mapped[object]:
        return mapped_column('date_created', DateTime, nullable=False)

    @declared_attr
    def user_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('user.id'), nullable=False)
    @declared_attr
    def user(cls) -> Mapped[object]:
        return relationship('User', foreign_keys='Chunk.user_id', lazy='select')
    @declared_attr
    def document_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('document.id'), nullable=False)
    @declared_attr
    def document(cls) -> Mapped[object]:
        return relationship('Document', foreign_keys='Chunk.document_id', lazy='select')
