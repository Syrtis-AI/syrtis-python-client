from sqlalchemy import ForeignKey, Integer, JSON, String, Uuid
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class SlotMessageGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'slot_message'

    @declared_attr
    def position(cls) -> Mapped[object]:
        return mapped_column(Integer, nullable=False)
    @declared_attr
    def type(cls) -> Mapped[object]:
        return mapped_column(String(120), nullable=False)
    @declared_attr
    def entity_metadata(cls) -> Mapped[object]:
        return mapped_column('metadata', JSON, nullable=True)
    @declared_attr
    def source(cls) -> Mapped[object]:
        return mapped_column(String(60), nullable=True)
    @declared_attr
    def orderBy(cls) -> Mapped[object]:
        return mapped_column('order_by', String(60), nullable=True)
    @declared_attr
    def orderDirection(cls) -> Mapped[object]:
        return mapped_column('order_direction', String(4), nullable=True)
    @declared_attr
    def format(cls) -> Mapped[object]:
        return mapped_column(String(120), nullable=True)
    @declared_attr
    def contentType(cls) -> Mapped[object]:
        return mapped_column('content_type', String(30), nullable=True)
    @declared_attr
    def name(cls) -> Mapped[object]:
        return mapped_column(String(255), nullable=True)
    @declared_attr
    def max(cls) -> Mapped[object]:
        return mapped_column(Integer, nullable=True)
    @declared_attr
    def direction(cls) -> Mapped[object]:
        return mapped_column(String(6), nullable=True)
    @declared_attr
    def collection(cls) -> Mapped[object]:
        return mapped_column(String(60), nullable=False)

    @declared_attr
    def template_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('template.id'), nullable=True)
    @declared_attr
    def template(cls) -> Mapped[object]:
        return relationship('Template', foreign_keys='SlotMessage.template_id', lazy='select')
    @declared_attr
    def slot_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('slot.id'), nullable=False)
    @declared_attr
    def slot(cls) -> Mapped[object]:
        return relationship('Slot', foreign_keys='SlotMessage.slot_id', back_populates='slotMessages', lazy='select')
    @declared_attr
    def message_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('message.id'), nullable=True)
    @declared_attr
    def message(cls) -> Mapped[object]:
        return relationship('Message', foreign_keys='SlotMessage.message_id', lazy='select')
    @declared_attr
    def slotMessageStamps(cls) -> Mapped[list['SlotMessageStamp']]:
        return relationship('SlotMessageStamp', foreign_keys='SlotMessageStamp.slot_message_id', back_populates='slotMessage', lazy='select')
