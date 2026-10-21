from sqlalchemy import DateTime, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class CardGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'card'

    @declared_attr
    def title(cls) -> Mapped[object]:
        return mapped_column(String(255), nullable=False)
    @declared_attr
    def dateCreated(cls) -> Mapped[object]:
        return mapped_column('date_created', DateTime, nullable=False)
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
    def scope(cls) -> Mapped[object]:
        return mapped_column(String(30), nullable=False)

    @declared_attr
    def user_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('user.id'), nullable=False)
    @declared_attr
    def user(cls) -> Mapped[object]:
        return relationship('User', foreign_keys='Card.user_id', lazy='select')
    @declared_attr
    def scenario_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('scenario.id'), nullable=False)
    @declared_attr
    def scenario(cls) -> Mapped[object]:
        return relationship('Scenario', foreign_keys='Card.scenario_id', back_populates='cards', lazy='select')
    @declared_attr
    def job_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('job.id'), nullable=True)
    @declared_attr
    def job(cls) -> Mapped[object]:
        return relationship('Job', foreign_keys='Card.job_id', lazy='select')
    @declared_attr
    def cardRelationsSources(cls) -> Mapped[list['CardRelation']]:
        return relationship('CardRelation', foreign_keys='CardRelation.card_source_id', back_populates='cardSource', lazy='select')
    @declared_attr
    def cardRelationsTarget(cls) -> Mapped[list['CardRelation']]:
        return relationship('CardRelation', foreign_keys='CardRelation.card_target_id', back_populates='cardTarget', lazy='select')
    @declared_attr
    def cardMessages(cls) -> Mapped[list['CardMessage']]:
        return relationship('CardMessage', foreign_keys='CardMessage.card_id', back_populates='card', lazy='select')
    @declared_attr
    def defaultEntrypointForScenarios(cls) -> Mapped[list['Scenario']]:
        return relationship('Scenario', foreign_keys='Scenario.default_entrypoint_id', back_populates='defaultEntrypoint', lazy='select')
