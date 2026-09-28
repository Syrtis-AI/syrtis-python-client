from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.template_generated import (
    TemplateGenerated,
)

__all__ = ["Template", "TemplateGenerated"]


class Template(TemplateGenerated, AbstractEntity):
    pass
