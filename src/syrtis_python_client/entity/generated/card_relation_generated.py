from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class CardRelationGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'card_relation'

    @declared_attr
    def secureId(cls) -> Mapped[object]:
        return mapped_column('secure_id', String(255), nullable=False)

    @declared_attr
    def card_source_id(cls) -> Mapped[object]:
        return mapped_column(Integer, ForeignKey('card.id'), nullable=False)
    @declared_attr
    def cardSource(cls) -> Mapped[object]:
        return relationship('Card', foreign_keys='CardRelation.card_source_id', back_populates='cardRelationsSources', lazy='select')
    @declared_attr
    def card_target_id(cls) -> Mapped[object]:
        return mapped_column(Integer, ForeignKey('card.id'), nullable=False)
    @declared_attr
    def cardTarget(cls) -> Mapped[object]:
        return relationship('Card', foreign_keys='CardRelation.card_target_id', back_populates='cardRelationsTarget', lazy='select')
