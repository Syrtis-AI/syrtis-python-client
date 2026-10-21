from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, Text, Uuid
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class ScenarioGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'scenario'

    @declared_attr
    def dateCreated(cls) -> Mapped[object]:
        return mapped_column('date_created', DateTime, nullable=False)
    @declared_attr
    def title(cls) -> Mapped[object]:
        return mapped_column(String(255), nullable=False)
    @declared_attr
    def description(cls) -> Mapped[object]:
        return mapped_column(Text, nullable=True)
    @declared_attr
    def secureId(cls) -> Mapped[object]:
        return mapped_column('secure_id', String(255), nullable=False)
    @declared_attr
    def positionX(cls) -> Mapped[object]:
        return mapped_column('position_x', Integer, nullable=True)
    @declared_attr
    def positionY(cls) -> Mapped[object]:
        return mapped_column('position_y', Integer, nullable=True)
    @declared_attr
    def zoom(cls) -> Mapped[object]:
        return mapped_column(Float, nullable=True)

    @declared_attr
    def user_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('user.id'), nullable=False)
    @declared_attr
    def user(cls) -> Mapped[object]:
        return relationship('User', foreign_keys='Scenario.user_id', lazy='select')
    @declared_attr
    def project_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, nullable=False)
    @declared_attr
    def environment_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('environment.id'), nullable=False)
    @declared_attr
    def environment(cls) -> Mapped[object]:
        return relationship('Environment', foreign_keys='Scenario.environment_id', lazy='select')
    @declared_attr
    def cards(cls) -> Mapped[list['Card']]:
        return relationship('Card', foreign_keys='Card.scenario_id', back_populates='scenario', lazy='select')
    @declared_attr
    def jobs(cls) -> Mapped[list['Job']]:
        return relationship('Job', foreign_keys='Job.scenario_id', back_populates='scenario', lazy='select')
    @declared_attr
    def default_entrypoint_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('card.id'), nullable=True)
    @declared_attr
    def defaultEntrypoint(cls) -> Mapped[object]:
        return relationship('Card', foreign_keys='Scenario.default_entrypoint_id', back_populates='defaultEntrypointForScenarios', lazy='select')
