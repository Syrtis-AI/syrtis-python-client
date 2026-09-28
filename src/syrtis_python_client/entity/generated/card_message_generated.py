from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class CardMessageGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'card_message'

    @declared_attr
    def card_id(cls) -> Mapped[object]:
        return mapped_column(Integer, ForeignKey('card.id'), nullable=False)
    @declared_attr
    def card(cls) -> Mapped[object]:
        return relationship('Card', foreign_keys='CardMessage.card_id', back_populates='cardMessages', lazy='select')
    @declared_attr
    def message_id(cls) -> Mapped[object]:
        return mapped_column(Integer, ForeignKey('message.id'), nullable=False)
    @declared_attr
    def message(cls) -> Mapped[object]:
        return relationship('Message', foreign_keys='CardMessage.message_id', lazy='select')
