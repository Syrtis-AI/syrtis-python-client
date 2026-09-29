from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.chunk_generated import (
    ChunkGenerated,
)

__all__ = ["Chunk", "ChunkGenerated"]


class Chunk(ChunkGenerated, AbstractEntity):
    pass
