from sqlalchemy import Boolean, DateTime, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, declared_attr, mapped_column


class UserGenerated:
    @classmethod
    def get_entity_name(cls) -> str:
        return 'user'

    @declared_attr
    def secureId(cls) -> Mapped[object]:
        return mapped_column('secure_id', String(255), nullable=False)
    @declared_attr
    def firstName(cls) -> Mapped[object]:
        return mapped_column('first_name', String(100), nullable=True)
    @declared_attr
    def lastName(cls) -> Mapped[object]:
        return mapped_column('last_name', String(100), nullable=True)
    @declared_attr
    def email(cls) -> Mapped[object]:
        return mapped_column(String(180), nullable=False, unique=True)
    @declared_attr
    def username(cls) -> Mapped[object]:
        return mapped_column(String(30), nullable=True, unique=True)
    @declared_attr
    def password(cls) -> Mapped[object]:
        return mapped_column(String, nullable=True)
    @declared_attr
    def roles(cls) -> Mapped[object]:
        return mapped_column(JSON, nullable=False)
    @declared_attr
    def enabled(cls) -> Mapped[object]:
        return mapped_column(Boolean, nullable=False)
    @declared_attr
    def locked(cls) -> Mapped[object]:
        return mapped_column(Boolean, nullable=False)
    @declared_attr
    def dateLastLogin(cls) -> Mapped[object]:
        return mapped_column('date_last_login', String, nullable=True)
    @declared_attr
    def passwordChangeRequired(cls) -> Mapped[object]:
        return mapped_column('password_change_required', Boolean, nullable=False)
    @declared_attr
    def emailTwoFactorEnabled(cls) -> Mapped[object]:
        return mapped_column('email_two_factor_enabled', Boolean, nullable=False)
    @declared_attr
    def trustedTokenVersion(cls) -> Mapped[object]:
        return mapped_column('trusted_token_version', Integer, nullable=False)
    @declared_attr
    def totpSecretEncrypted(cls) -> Mapped[object]:
        return mapped_column('totp_secret_encrypted', Text, nullable=True)
    @declared_attr
    def backupCodes(cls) -> Mapped[object]:
        return mapped_column('backup_codes', JSON, nullable=False)
    @declared_attr
    def dateCreated(cls) -> Mapped[object]:
        return mapped_column('date_created', DateTime, nullable=False)
    @declared_attr
    def locale(cls) -> Mapped[object]:
        return mapped_column(String(12), nullable=True)
