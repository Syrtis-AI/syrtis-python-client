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

    FORMAT_BOOLEAN = "boolean"
    FORMAT_FLOAT = "float"
    FORMAT_HTML = "html"
    FORMAT_INTEGER = "integer"
    FORMAT_JSON = "json"
    FORMAT_MARKDOWN = "markdown"
    FORMAT_NULL = "null"
    FORMAT_TEXT = "text"
    FORMAT_YAML = "yaml"
    # filestate: python-iterable-sort
    FORMATS = [
        FORMAT_BOOLEAN,
        FORMAT_FLOAT,
        FORMAT_HTML,
        FORMAT_INTEGER,
        FORMAT_JSON,
        FORMAT_MARKDOWN,
        FORMAT_NULL,
        FORMAT_TEXT,
        FORMAT_YAML,
    ]

    CONTENT_TYPE_ACTIONS = "core/actions"
    CONTENT_TYPE_ANALYSIS = "core/analysis"
    CONTENT_TYPE_CONVERSATION = "core/conversation"
    CONTENT_TYPE_DEBUG = "core/debug"
    CONTENT_TYPE_DEFAULT = "core/default"
    CONTENT_TYPE_DOWNLOAD = "core/download"
    CONTENT_TYPE_ERROR = "core/error"
    CONTENT_TYPE_FORM = "core/form"
    CONTENT_TYPE_HTTP_RESPONSE = "core/http_response"
    CONTENT_TYPE_IMAGE = "core/image"
    CONTENT_TYPE_INFO = "core/info"
    CONTENT_TYPE_LIST = "core/list"
    CONTENT_TYPE_NAVIGATE = "core/navigate"
    CONTENT_TYPE_NAVIGATED = "core/navigated"
    CONTENT_TYPE_PROGRESS = "core/progress"
    CONTENT_TYPE_REFERENCE = "core/reference"
    CONTENT_TYPE_SESSION = "core/session"
    CONTENT_TYPE_SESSION_EXPIRE = "core/session_expire"
    CONTENT_TYPE_SESSION_STATUS = "core/session_status"
    CONTENT_TYPE_SUCCESS = "core/success"
    CONTENT_TYPE_THOUGHT = "core/thought"
    CONTENT_TYPE_TOOL_CALL = "core/tool_call"
    CONTENT_TYPE_UPLOAD = "core/upload"
    CONTENT_TYPE_URL = "core/url"
    CONTENT_TYPE_VIDEO = "core/video"
    CONTENT_TYPE_WARNING = "core/warning"
    # filestate: python-iterable-sort
    CONTENT_TYPES = [
        CONTENT_TYPE_ACTIONS,
        CONTENT_TYPE_ANALYSIS,
        CONTENT_TYPE_CONVERSATION,
        CONTENT_TYPE_DEBUG,
        CONTENT_TYPE_DEFAULT,
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
        CONTENT_TYPE_SESSION,
        CONTENT_TYPE_SESSION_EXPIRE,
        CONTENT_TYPE_SESSION_STATUS,
        CONTENT_TYPE_SUCCESS,
        CONTENT_TYPE_THOUGHT,
        CONTENT_TYPE_TOOL_CALL,
        CONTENT_TYPE_UPLOAD,
        CONTENT_TYPE_URL,
        CONTENT_TYPE_VIDEO,
        CONTENT_TYPE_WARNING,
    ]

    def get_formatted_content(self, format: str | None = None) -> Any:
        format = format or self.format

        if format == self.FORMAT_JSON:
            from wexample_helpers.helper.json import json_parse_if_valid

            return json_parse_if_valid(self.content)
        if format == self.FORMAT_INTEGER:
            return int(self.content)
        if format == self.FORMAT_FLOAT:
            return float(self.content)
        if format == self.FORMAT_BOOLEAN:
            return (self.content or "").lower() in ["true", "1", "yes"]
        if format == self.FORMAT_NULL:
            return None
        if format == self.FORMAT_YAML:
            import yaml

            return yaml.safe_load(self.content)
        return self.content

    def get_stamps_names(self) -> list[str]:
        return [stamp.name for stamp in self.stamps]

    def has_stamps_name(self, stamp_name: str | list[str]) -> bool:
        """A list requires every stamp to be present."""
        names = self.get_stamps_names()
        required = [stamp_name] if isinstance(stamp_name, str) else stamp_name
        return all(name in names for name in required)

    def is_chat_message_from_assistant(self) -> bool:
        return self.origin != self.ORIGIN_USER and self.has_stamps_name("chat")
