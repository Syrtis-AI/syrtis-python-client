from __future__ import annotations

from wexample_orm.entity.abstract_entity import AbstractEntity

from syrtis_python_client.entity.generated.job_generated import JobGenerated

__all__ = ["Job", "JobGenerated"]


class Job(JobGenerated, AbstractEntity):
    def get_end_slot(self):
        from syrtis_python_client.entity.slot import Slot

        return self.get_slot_by_type(Slot.TYPE_END)

    def get_slot_by_type(self, type: str):
        for slot in self.slots:
            if slot.type == type:
                return slot
        return None

    def get_start_slot(self):
        from syrtis_python_client.entity.slot import Slot

        return self.get_slot_by_type(Slot.TYPE_START)
