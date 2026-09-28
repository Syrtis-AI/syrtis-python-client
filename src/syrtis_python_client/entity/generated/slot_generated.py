from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class SlotGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'slot'

    @declared_attr
    def type(cls) -> Mapped[object]:
        return mapped_column(String(120), nullable=False)
    @declared_attr
    def title(cls) -> Mapped[object]:
        return mapped_column(String(255), nullable=False)
    @declared_attr
    def secureId(cls) -> Mapped[object]:
        return mapped_column('secure_id', String(255), nullable=False)
    @declared_attr
    def positionX(cls) -> Mapped[object]:
        return mapped_column('position_x', Integer, nullable=False)
    @declared_attr
    def positionY(cls) -> Mapped[object]:
        return mapped_column('position_y', Integer, nullable=False)

    @declared_attr
    def job_id(cls) -> Mapped[object]:
        return mapped_column(Integer, ForeignKey('job.id'), nullable=False)
    @declared_attr
    def job(cls) -> Mapped[object]:
        return relationship('Job', foreign_keys='Slot.job_id', back_populates='slots', lazy='select')
    @declared_attr
    def node_id(cls) -> Mapped[object]:
        return mapped_column(Integer, ForeignKey('node.id'), nullable=False)
    @declared_attr
    def node(cls) -> Mapped[object]:
        return relationship('Node', foreign_keys='Slot.node_id', lazy='select')
    @declared_attr
    def slotRelationsSources(cls) -> Mapped[list['SlotRelation']]:
        return relationship('SlotRelation', foreign_keys='SlotRelation.slot_source_id', back_populates='slotSource', lazy='select')
    @declared_attr
    def slotRelationsTargets(cls) -> Mapped[list['SlotRelation']]:
        return relationship('SlotRelation', foreign_keys='SlotRelation.slot_target_id', back_populates='slotTarget', lazy='select')
    @declared_attr
    def slotConfigs(cls) -> Mapped[list['SlotConfig']]:
        return relationship('SlotConfig', foreign_keys='SlotConfig.slot_id', back_populates='slot', lazy='select')
    @declared_attr
    def slotMessages(cls) -> Mapped[list['SlotMessage']]:
        return relationship('SlotMessage', foreign_keys='SlotMessage.slot_id', back_populates='slot', lazy='select')
