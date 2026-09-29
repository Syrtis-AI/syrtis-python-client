from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.document_generated import (
    DocumentGenerated,
)

__all__ = ["Document", "DocumentGenerated"]


class Document(DocumentGenerated, AbstractEntity):
    # Its content is split into chunks, not held by the document itself.
    TYPE_CHUNKS = "chunks"
    # Its content is a file, kept by a storage.
    TYPE_FILE = "file"
    TYPE_TEXT = "text"
