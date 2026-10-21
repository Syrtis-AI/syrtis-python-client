from sqlalchemy import ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class SlotRelationGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'slot_relation'

    @declared_attr
    def portSource(cls) -> Mapped[object]:
        return mapped_column('port_source', String(60), nullable=False)
    @declared_attr
    def portTarget(cls) -> Mapped[object]:
        return mapped_column('port_target', String(60), nullable=False)

    @declared_attr
    def slot_source_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('slot.id'), nullable=False)
    @declared_attr
    def slotSource(cls) -> Mapped[object]:
        return relationship('Slot', foreign_keys='SlotRelation.slot_source_id', back_populates='slotRelationsSources', lazy='select')
    @declared_attr
    def slot_target_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('slot.id'), nullable=False)
    @declared_attr
    def slotTarget(cls) -> Mapped[object]:
        return relationship('Slot', foreign_keys='SlotRelation.slot_target_id', back_populates='slotRelationsTargets', lazy='select')
