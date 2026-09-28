from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class SlotMessageStampGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'slot_message_stamp'

    @declared_attr
    def name(cls) -> Mapped[object]:
        return mapped_column(String(255), nullable=False)

    @declared_attr
    def slot_message_id(cls) -> Mapped[object]:
        return mapped_column(Integer, ForeignKey('slot_message.id'), nullable=False)
    @declared_attr
    def slotMessage(cls) -> Mapped[object]:
        return relationship('SlotMessage', foreign_keys='SlotMessageStamp.slot_message_id', back_populates='slotMessageStamps', lazy='select')
