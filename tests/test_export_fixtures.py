"""Every export fixture of the API (a snapshot, see bin/sync-fixtures.py)
imports into this client's entities and exports back without loss."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

FIXTURES_DIR = Path(__file__).parent / "fixtures" / "export"
FIXTURES = [
    pytest.param(path, id=f"{path.parent.name}/{path.stem}")
    for path in sorted(FIXTURES_DIR.glob("*/*.json"))
]


def get_entity_types() -> list:
    from sqlalchemy.orm import configure_mappers
    from syrtis_python_client.common.generated_entities import all_entities

    configure_mappers()
    return all_entities


def import_document(document: dict):
    from wexample_orm.import_export.entity_importer import EntityImporter

    importer = EntityImporter(entity_types=get_entity_types(), assign_ids=True)
    [root] = importer.import_document(document)
    return importer, root


def export_document(root) -> dict:
    from wexample_orm.import_export.entity_exporter import EntityExporter

    return EntityExporter(version="test").export_document(root)


def test_fixtures_are_synced() -> None:
    assert FIXTURES, "No fixture: run bin/sync-fixtures.py"


@pytest.mark.parametrize("fixture", FIXTURES)
def test_fixture_imports_and_exports_back(fixture: Path) -> None:
    importer, root = import_document(json.loads(fixture.read_text(encoding="utf-8")))
    known = {entity_type.get_entity_name() for entity_type in get_entity_types()}

    # Only references to entities this client does not carry may be left aside.
    for warning in importer.warnings:
        relation = warning.split(".", 1)[1].split("_", 1)[0]
        assert re.sub(r"(?<!^)(?=[A-Z])", "_", relation).lower() not in known, warning

    exported = export_document(root)
    reimporter, reimported = import_document(exported)

    assert len(reimporter.get_entities()) == len(importer.get_entities())
    assert export_document(reimported) == exported
