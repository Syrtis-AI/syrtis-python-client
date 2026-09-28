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

    def get_end_cards(self) -> list:
        """Cards no relation leaves, by id."""
        return sorted(
            (card for card in self.cards if not card.cardRelationsSources),
            key=lambda card: card.id,
        )

    def get_entrypoint_cards(self) -> list:
        """Cards no relation reaches, by id."""
        return sorted(
            (card for card in self.cards if not card.cardRelationsTarget),
            key=lambda card: card.id,
        )

    def find_card(self, card_id: int):
        for card in self.cards:
            if card.id == card_id:
                return card
        return None

    def find_job(self, job_id: int):
        """A job of the scenario, its own or one of its cards'."""
        for job in [*self.jobs, *(card.job for card in self.cards if card.job is not None)]:
            if job.id == job_id:
                return job
        return None
