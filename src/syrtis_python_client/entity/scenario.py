from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.scenario_generated import ScenarioGenerated

__all__ = ["Scenario", "ScenarioGenerated"]


class Scenario(ScenarioGenerated, AbstractEntity):
    def get_messages(self) -> list:
        """The messages every step of the scenario is given."""
        return [relation.message for relation in self.scenarioMessages if relation.message is not None]

    def find_step(self, step_id):
        for step in self.steps:
            if str(step.id) == str(step_id):
                return step
        return None

    def find_job(self, job_id):
        """A job of the scenario, its own or one of its steps'."""
        for job in [*self.jobs, *(step.job for step in self.steps if step.job is not None)]:
            if str(job.id) == str(job_id):
                return job
        return None
