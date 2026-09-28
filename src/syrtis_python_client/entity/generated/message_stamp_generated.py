from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class MessageStampGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'message_stamp'

    @declared_attr
    def name(cls) -> Mapped[object]:
        return mapped_column(String(255), nullable=False)
    @declared_attr
    def secureId(cls) -> Mapped[object]:
        return mapped_column('secure_id', String(255), nullable=False)

    @declared_attr
    def message_id(cls) -> Mapped[object]:
        return mapped_column(Integer, ForeignKey('message.id'), nullable=False)
    @declared_attr
    def message(cls) -> Mapped[object]:
        return relationship('Message', foreign_keys='MessageStamp.message_id', back_populates='stamps', lazy='select')
