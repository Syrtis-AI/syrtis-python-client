from sqlalchemy import DateTime, ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class StepGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'step'

    @declared_attr
    def title(cls) -> Mapped[object]:
        return mapped_column(String(255), nullable=False)
    @declared_attr
    def dateCreated(cls) -> Mapped[object]:
        return mapped_column('date_created', DateTime, nullable=False)

    @declared_attr
    def user_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('user.id'), nullable=False)
    @declared_attr
    def user(cls) -> Mapped[object]:
        return relationship('User', foreign_keys='Step.user_id', lazy='select')
    @declared_attr
    def scenario_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('scenario.id'), nullable=False)
    @declared_attr
    def scenario(cls) -> Mapped[object]:
        return relationship('Scenario', foreign_keys='Step.scenario_id', back_populates='steps', lazy='select')
    @declared_attr
    def job_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('job.id'), nullable=True)
    @declared_attr
    def job(cls) -> Mapped[object]:
        return relationship('Job', foreign_keys='Step.job_id', lazy='select')
    @declared_attr
    def stepMessages(cls) -> Mapped[list['StepMessage']]:
        return relationship('StepMessage', foreign_keys='StepMessage.step_id', back_populates='step', lazy='select')
    @declared_attr
    def defaultEntrypointForScenarios(cls) -> Mapped[list['Scenario']]:
        return relationship('Scenario', foreign_keys='Scenario.default_entrypoint_id', back_populates='defaultEntrypoint', lazy='select')
