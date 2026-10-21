from sqlalchemy import DateTime, ForeignKey, String, Text, Uuid
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class TemplateGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'template'

    @declared_attr
    def dateCreated(cls) -> Mapped[object]:
        return mapped_column('date_created', DateTime, nullable=False)
    @declared_attr
    def name(cls) -> Mapped[object]:
        return mapped_column(String(255), nullable=False)
    @declared_attr
    def content(cls) -> Mapped[object]:
        return mapped_column(Text, nullable=True)
    @declared_attr
    def secureId(cls) -> Mapped[object]:
        return mapped_column('secure_id', String(255), nullable=False)

    @declared_attr
    def scenario_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('scenario.id'), nullable=False)
    @declared_attr
    def scenario(cls) -> Mapped[object]:
        return relationship('Scenario', foreign_keys='Template.scenario_id', lazy='select')
