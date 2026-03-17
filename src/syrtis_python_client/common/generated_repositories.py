from __future__ import annotations

from syrtis_python_client.repository.message_repository import MessageRepository
from syrtis_python_client.repository.message_stamp_repository import MessageStampRepository
from syrtis_python_client.repository.request_repository import RequestRepository
from syrtis_python_client.repository.session_repository import SessionRepository
from syrtis_python_client.repository.user_repository import UserRepository


generated_repositories = [
    MessageRepository,
    MessageStampRepository,
    RequestRepository,
    SessionRepository,
    UserRepository,
]
