from sqlalchemy import ForeignKey, Uuid
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class StepMessageGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'step_message'

    @declared_attr
    def step_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('step.id'), nullable=False)
    @declared_attr
    def step(cls) -> Mapped[object]:
        return relationship('Step', foreign_keys='StepMessage.step_id', back_populates='stepMessages', lazy='select')
    @declared_attr
    def message_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('message.id'), nullable=False)
    @declared_attr
    def message(cls) -> Mapped[object]:
        return relationship('Message', foreign_keys='StepMessage.message_id', lazy='select')
