from __future__ import annotations

from typing import Any

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.message_generated import MessageGenerated

__all__ = ["Message", "MessageGenerated"]


class Message(MessageGenerated, AbstractEntity):
    ORIGIN_STEP = "step"
    ORIGIN_SCENARIO = "scenario"
    ORIGIN_CORE = "core"
    ORIGIN_NODE = "node"
    ORIGIN_USER = "user"

    # filestate: python-iterable-sort

    CONTENT_TYPE_ACTIONS = "conversation/actions"
    CONTENT_TYPE_ANALYSIS = "core/analysis"
    CONTENT_TYPE_CONVERSATION_MESSAGE = "conversation/message"
    CONTENT_TYPE_DEBUG = "core/debug"
    CONTENT_TYPE_DOWNLOAD = "core/download"
    CONTENT_TYPE_ERROR = "core/error"
    CONTENT_TYPE_FORM = "core/form"
    CONTENT_TYPE_HTTP_RESPONSE = "core/http_response"
    CONTENT_TYPE_IMAGE = "core/image"
    CONTENT_TYPE_INFO = "web/info"
    CONTENT_TYPE_LIST = "core/list"
    CONTENT_TYPE_NAVIGATE = "core/navigate"
    CONTENT_TYPE_NAVIGATED = "core/navigated"
    CONTENT_TYPE_PROGRESS = "core/progress"
    CONTENT_TYPE_REFERENCE = "core/reference"
    CONTENT_TYPE_SESSION_EXPIRE = "core/session_expire"
    CONTENT_TYPE_SESSION_STATUS = "core/session_status"
    CONTENT_TYPE_SUCCESS = "web/success"
    CONTENT_TYPE_THOUGHT = "conversation/thought"
    CONTENT_TYPE_TOOL_CALL = "core/tool_call"
    CONTENT_TYPE_UPLOAD = "core/upload"
    CONTENT_TYPE_URL = "core/url"
    CONTENT_TYPE_VIDEO = "core/video"
    CONTENT_TYPE_WARNING = "core/warning"
    # The types of a message's shape alone: a text, a value as JSON.
    CONTENT_TYPE_TEXT = "content/text"
    CONTENT_TYPE_MARKDOWN = "content/markdown"
    CONTENT_TYPE_HTML = "content/html"
    CONTENT_TYPE_YAML = "content/yaml"
    CONTENT_TYPE_JSON = "content/json"
    # filestate: python-iterable-sort
    CONTENT_TYPES = [
        CONTENT_TYPE_ACTIONS,
        CONTENT_TYPE_ANALYSIS,
        CONTENT_TYPE_CONVERSATION_MESSAGE,
        CONTENT_TYPE_DEBUG,
        CONTENT_TYPE_DOWNLOAD,
        CONTENT_TYPE_ERROR,
        CONTENT_TYPE_FORM,
        CONTENT_TYPE_HTTP_RESPONSE,
        CONTENT_TYPE_IMAGE,
        CONTENT_TYPE_INFO,
        CONTENT_TYPE_LIST,
        CONTENT_TYPE_NAVIGATE,
        CONTENT_TYPE_NAVIGATED,
        CONTENT_TYPE_PROGRESS,
        CONTENT_TYPE_REFERENCE,
        CONTENT_TYPE_SESSION_EXPIRE,
        CONTENT_TYPE_SESSION_STATUS,
        CONTENT_TYPE_SUCCESS,
        CONTENT_TYPE_THOUGHT,
        CONTENT_TYPE_TOOL_CALL,
        CONTENT_TYPE_UPLOAD,
        CONTENT_TYPE_URL,
        CONTENT_TYPE_VIDEO,
        CONTENT_TYPE_WARNING,
        CONTENT_TYPE_TEXT,
        CONTENT_TYPE_MARKDOWN,
        CONTENT_TYPE_HTML,
        CONTENT_TYPE_YAML,
        CONTENT_TYPE_JSON,
    ]

    def get_formatted_content(self) -> Any:
        """The content as its type reads it: what the api read of it
        (`formattedContent`) when it came with the message; the JSON it
        encodes when it decodes, the text otherwise."""
        formatted = getattr(self, "formattedContent", None)
        if formatted is not None:
            return formatted

        if self.content is None:
            return None

        import json

        try:
            return json.loads(self.content)
        except ValueError:
            return self.content

    def get_stamps_names(self) -> list[str]:
        return [stamp.name for stamp in self.stamps]

    def has_stamps_name(self, stamp_name: str | list[str]) -> bool:
        """A list requires every stamp to be present."""
        names = self.get_stamps_names()
        required = [stamp_name] if isinstance(stamp_name, str) else stamp_name
        return all(name in names for name in required)

    def is_chat_message_from_assistant(self) -> bool:
        """A turn of the conversation the agent said: what a chat shows as its reply,
        as the other clients tell it (`isReply`)."""
        return (
            self.origin != self.ORIGIN_USER
            and self.content_type == self.CONTENT_TYPE_CONVERSATION_MESSAGE
        )
