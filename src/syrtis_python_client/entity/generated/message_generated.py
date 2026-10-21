from sqlalchemy import DateTime, ForeignKey, Integer, JSON, String, Text, Uuid
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship


class MessageGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'message'

    @declared_attr
    def content(cls) -> Mapped[object]:
        return mapped_column(Text, nullable=True)
    @declared_attr
    def contentType(cls) -> Mapped[object]:
        return mapped_column('content_type', String(30), nullable=False)
    @declared_attr
    def dateCreated(cls) -> Mapped[object]:
        return mapped_column('date_created', DateTime, nullable=False)
    @declared_attr
    def format(cls) -> Mapped[object]:
        return mapped_column(String(120), nullable=False)
    @declared_attr
    def name(cls) -> Mapped[object]:
        return mapped_column(String(255), nullable=True)
    @declared_attr
    def origin(cls) -> Mapped[object]:
        return mapped_column(String(30), nullable=False)
    @declared_attr
    def secureId(cls) -> Mapped[object]:
        return mapped_column('secure_id', String(255), nullable=False)
    @declared_attr
    def versionMajor(cls) -> Mapped[object]:
        return mapped_column('version_major', Integer, nullable=False)
    @declared_attr
    def versionMinor(cls) -> Mapped[object]:
        return mapped_column('version_minor', Integer, nullable=False)
    @declared_attr
    def entity_metadata(cls) -> Mapped[object]:
        return mapped_column('metadata', JSON, nullable=True)

    @declared_attr
    def target_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('message.id'), nullable=True)
    @declared_attr
    def target(cls) -> Mapped[object]:
        return relationship('Message', foreign_keys='Message.target_id', lazy='select')
    @declared_attr
    def request_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('request.id'), nullable=True)
    @declared_attr
    def request(cls) -> Mapped[object]:
        return relationship('Request', foreign_keys='Message.request_id', back_populates='messages', lazy='select')
    @declared_attr
    def session_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('session.id'), nullable=True)
    @declared_attr
    def session(cls) -> Mapped[object]:
        return relationship('Session', foreign_keys='Message.session_id', back_populates='messages', lazy='select')
    @declared_attr
    def model_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, nullable=True)
    @declared_attr
    def slot_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('slot.id'), nullable=True)
    @declared_attr
    def slot(cls) -> Mapped[object]:
        return relationship('Slot', foreign_keys='Message.slot_id', lazy='select')
    @declared_attr
    def expiration_message_id(cls) -> Mapped[object]:
        return mapped_column(Uuid, ForeignKey('message.id'), nullable=True)
    @declared_attr
    def expirationMessage(cls) -> Mapped[object]:
        return relationship('Message', foreign_keys='Message.expiration_message_id', lazy='select')
    @declared_attr
    def stamps(cls) -> Mapped[list['MessageStamp']]:
        return relationship('MessageStamp', foreign_keys='MessageStamp.message_id', back_populates='message', lazy='select')
