from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.scenario_generated import ScenarioGenerated

__all__ = ["Scenario", "ScenarioGenerated"]


class Scenario(ScenarioGenerated, AbstractEntity):
    def get_global_card(self):
        for card in self.cards:
            if card.scope == card.SCOPE_GLOBAL:
                return card
        return None
