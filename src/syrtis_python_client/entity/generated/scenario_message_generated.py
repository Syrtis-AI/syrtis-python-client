from sqlalchemy import ForeignKey, Uuid
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class ScenarioMessageGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'scenario_message'

    @declared_attr
    def scenario_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('scenario.id'), nullable=False)
    @declared_attr
    def scenario(cls) -> Mapped[object]:
        return relationship('Scenario', foreign_keys='ScenarioMessage.scenario_id', back_populates='scenarioMessages', lazy='select')
    @declared_attr
    def message_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('message.id'), nullable=False)
    @declared_attr
    def message(cls) -> Mapped[object]:
        return relationship('Message', foreign_keys='ScenarioMessage.message_id', lazy='select')
