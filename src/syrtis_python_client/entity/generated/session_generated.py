from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class SessionGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'session'

    @declared_attr
    def dateCreated(cls) -> Mapped[object]:
        return mapped_column('date_created', DateTime, nullable=False)
    @declared_attr
    def secureId(cls) -> Mapped[object]:
        return mapped_column('secure_id', String(255), nullable=False)
    @declared_attr
    def status(cls) -> Mapped[object]:
        return mapped_column(String(30), nullable=False)
    @declared_attr
    def title(cls) -> Mapped[object]:
        return mapped_column(String(255), nullable=False)
    @declared_attr
    def dateLastAccess(cls) -> Mapped[object]:
        return mapped_column('date_last_access', DateTime, nullable=True)

    @declared_attr
    def user_id(cls) -> Mapped[object]:
        return mapped_column(Integer, ForeignKey('user.id'), nullable=False)
    @declared_attr
    def user(cls) -> Mapped[object]:
        return relationship('User', foreign_keys='Session.user_id', lazy='select')
    @declared_attr
    def scenario_id(cls) -> Mapped[object]:
        return mapped_column(Integer, ForeignKey('scenario.id'), nullable=False)
    @declared_attr
    def scenario(cls) -> Mapped[object]:
        return relationship('Scenario', foreign_keys='Session.scenario_id', lazy='select')
    @declared_attr
    def requests(cls) -> Mapped[list['Request']]:
        return relationship('Request', foreign_keys='Request.session_id', back_populates='session', lazy='select')
    @declared_attr
    def messages(cls) -> Mapped[list['Message']]:
        return relationship('Message', foreign_keys='Message.session_id', back_populates='session', lazy='select')
    @declared_attr
    def session_group_id(cls) -> Mapped[object]:
        return mapped_column(Integer, nullable=False)
