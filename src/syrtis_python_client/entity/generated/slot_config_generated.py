from sqlalchemy import Boolean, ForeignKey, String, Text, Uuid
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class SlotConfigGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'slot_config'

    @declared_attr
    def value(cls) -> Mapped[object]:
        return mapped_column(Text, nullable=True)
    @declared_attr
    def expression(cls) -> Mapped[object]:
        return mapped_column(Boolean, nullable=False)
    @declared_attr
    def name(cls) -> Mapped[object]:
        return mapped_column(String(255), nullable=False)

    @declared_attr
    def slot_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('slot.id'), nullable=False)
    @declared_attr
    def slot(cls) -> Mapped[object]:
        return relationship('Slot', foreign_keys='SlotConfig.slot_id', back_populates='slotConfigs', lazy='select')
