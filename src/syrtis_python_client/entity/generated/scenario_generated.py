from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Text, Uuid
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
    def versionMajor(cls) -> Mapped[object]:
        return mapped_column('version_major', Integer, nullable=False)
    @declared_attr
    def versionMinor(cls) -> Mapped[object]:
        return mapped_column('version_minor', Integer, nullable=False)
    @declared_attr
    def lineage(cls) -> Mapped[object]:
        return mapped_column(Uuid, nullable=False)
    @declared_attr
    def datePublished(cls) -> Mapped[object]:
        return mapped_column('date_published', String, nullable=True)
    @declared_attr
    def archived(cls) -> Mapped[object]:
        return mapped_column(Boolean, nullable=False)

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
    def previous_version_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('scenario.id'), nullable=True)
    @declared_attr
    def previousVersion(cls) -> Mapped[object]:
        return relationship('Scenario', foreign_keys='Scenario.previous_version_id', lazy='select')
    @declared_attr
    def steps(cls) -> Mapped[list['Step']]:
        return relationship('Step', foreign_keys='Step.scenario_id', back_populates='scenario', lazy='select')
    @declared_attr
    def scenarioMessages(cls) -> Mapped[list['ScenarioMessage']]:
        return relationship('ScenarioMessage', foreign_keys='ScenarioMessage.scenario_id', back_populates='scenario', lazy='select')
    @declared_attr
    def jobs(cls) -> Mapped[list['Job']]:
        return relationship('Job', foreign_keys='Job.scenario_id', back_populates='scenario', lazy='select')
    @declared_attr
    def default_entrypoint_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('step.id'), nullable=True)
    @declared_attr
    def defaultEntrypoint(cls) -> Mapped[object]:
        return relationship('Step', foreign_keys='Scenario.default_entrypoint_id', back_populates='defaultEntrypointForScenarios', lazy='select')
