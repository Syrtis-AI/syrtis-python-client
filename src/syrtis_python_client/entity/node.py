from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.node_generated import (
    NodeGenerated,
)

__all__ = ["Node", "NodeGenerated"]


class Node(NodeGenerated, AbstractEntity):
    pass
