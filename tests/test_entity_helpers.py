from __future__ import annotations

from sqlalchemy.orm import configure_mappers
from wexample_orm.import_export.entity_importer import EntityImporter

from syrtis_python_client.common.generated_entities import all_entities


def import_scenario():
    configure_mappers()
    importer = EntityImporter(entity_types=all_entities, assign_ids=True)
    [scenario] = importer.import_document(
        {
            "type": "single",
            "entity": "scenario",
            "data": {
                "_ref": "scenario",
                "defaultEntrypoint_ref": "entry",
                "card": [
                    {
                        "_ref": "global",
                        "scope": "global",
                        "message": [
                            {
                                "content": '{"mode": "edit"}',
                                "format": "json",
                                "messageStamp": [{"name": "a"}, {"name": "b"}],
                            }
                        ],
                    },
                    {
                        "_ref": "entry",
                        "scope": "default",
                        "job": {
                            "slot": [
                                {"_ref": "end", "type": "end", "node_type": "null"},
                                {
                                    "_ref": "start",
                                    "type": "start",
                                    "node_type": "null",
                                    "slotConfig": [{"name": "x", "value": 1}],
                                    "slotMessage": [
                                        {
                                            "format": "json",
                                            "slotMessageStamp": [{"name": "a"}],
                                        }
                                    ],
                                },
                            ],
                            "slotRelation": [
                                {"slotSource_ref": "start", "slotTarget_ref": "end"}
                            ],
                        },
                    },
                ],
            },
        }
    )
    return scenario


def test_scenario_and_job_helpers() -> None:
    scenario = import_scenario()
    job = scenario.defaultEntrypoint.job

    assert scenario.get_global_card().scope == "global"
    assert job.get_start_slot().is_start()
    assert job.get_end_slot().is_end()
    assert [c.value for c in job.get_start_slot().get_configs_by_name("x")] == [1]


def test_message_and_selector_helpers() -> None:
    scenario = import_scenario()
    [message] = scenario.get_global_card().get_messages()
    [selector] = scenario.defaultEntrypoint.job.get_start_slot().slotMessages

    assert message.get_formatted_content() == {"mode": "edit"}
    assert message.has_stamps_name(["a", "b"])
    assert not message.has_stamps_name(["a", "c"])
    assert selector.matches(message)
