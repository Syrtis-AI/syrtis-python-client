from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class JobGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'job'

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
    def zoom(cls) -> Mapped[object]:
        return mapped_column(Float, nullable=True)
    @declared_attr
    def title(cls) -> Mapped[object]:
        return mapped_column(String(255), nullable=True)

    @declared_attr
    def user_id(cls) -> Mapped[object]:
        return mapped_column(Integer, ForeignKey('user.id'), nullable=False)
    @declared_attr
    def user(cls) -> Mapped[object]:
        return relationship('User', foreign_keys='Job.user_id', lazy='select')
    @declared_attr
    def scenario_id(cls) -> Mapped[object]:
        return mapped_column(Integer, ForeignKey('scenario.id'), nullable=True)
    @declared_attr
    def scenario(cls) -> Mapped[object]:
        return relationship('Scenario', foreign_keys='Job.scenario_id', back_populates='jobs', lazy='select')
    @declared_attr
    def slots(cls) -> Mapped[list['Slot']]:
        return relationship('Slot', foreign_keys='Slot.job_id', back_populates='job', lazy='select')
