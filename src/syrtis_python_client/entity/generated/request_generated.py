from sqlalchemy import DateTime, ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class RequestGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'request'

    @declared_attr
    def status(cls) -> Mapped[object]:
        return mapped_column(String(30), nullable=False)
    @declared_attr
    def dateCreated(cls) -> Mapped[object]:
        return mapped_column('date_created', DateTime, nullable=False)
    @declared_attr
    def secureId(cls) -> Mapped[object]:
        return mapped_column('secure_id', String(255), nullable=False)
    @declared_attr
    def type(cls) -> Mapped[object]:
        return mapped_column(String(120), nullable=False)
    @declared_attr
    def dateCompleted(cls) -> Mapped[object]:
        return mapped_column('date_completed', DateTime, nullable=True)
    @declared_attr
    def lastEvent(cls) -> Mapped[object]:
        return mapped_column('last_event', String(60), nullable=True)

    @declared_attr
    def parent_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('request.id'), nullable=True)
    @declared_attr
    def parent(cls) -> Mapped[object]:
        return relationship('Request', foreign_keys='Request.parent_id', back_populates='children', remote_side='Request.id', lazy='select')
    @declared_attr
    def children(cls) -> Mapped[list['Request']]:
        return relationship('Request', foreign_keys='Request.parent_id', back_populates='parent', lazy='select')
    @declared_attr
    def timezone_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('timezone.id'), nullable=False)
    @declared_attr
    def timezone(cls) -> Mapped[object]:
        return relationship('Timezone', foreign_keys='Request.timezone_id', lazy='select')
    @declared_attr
    def messages(cls) -> Mapped[list['Message']]:
        return relationship('Message', foreign_keys='Message.request_id', back_populates='request', lazy='select')
    @declared_attr
    def projection_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, nullable=True)
    @declared_attr
    def session_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('session.id'), nullable=True)
    @declared_attr
    def session(cls) -> Mapped[object]:
        return relationship('Session', foreign_keys='Request.session_id', back_populates='requests', lazy='select')
    @declared_attr
    def card_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('card.id'), nullable=True)
    @declared_attr
    def card(cls) -> Mapped[object]:
        return relationship('Card', foreign_keys='Request.card_id', lazy='select')
