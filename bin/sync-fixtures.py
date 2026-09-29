#!/usr/bin/env python3
"""Copy the API export fixtures of this client's entities into its tests.

    bin/sync-fixtures.py <api>/assets/fixtures/test/valid/single

The API owns the fixtures; the tests read a snapshot, so that they do not
depend on where the API sits. Run it again when the fixtures or the entities
change; entities of the other client are left to it."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1

    source_dir = Path(sys.argv[1]).resolve()
    root_dir = Path(__file__).resolve().parent.parent
    [package_dir] = [
        path for path in (root_dir / "src").iterdir() if path.name.startswith("syrtis_python_client")
    ]
    entity_names = {path.stem for path in (package_dir / "data" / "entity").glob("*.json")}
    target_dir = root_dir / "tests" / "fixtures" / "export"
    shutil.rmtree(target_dir, ignore_errors=True)

    copied = 0
    for entity_dir in sorted(path for path in source_dir.iterdir() if path.name in entity_names):
        (target_dir / entity_dir.name).mkdir(parents=True)
        for fixture in sorted(entity_dir.glob("*.json")):
            shutil.copy2(fixture, target_dir / entity_dir.name / fixture.name)
            copied += 1
    print(f"Fixtures copied: {copied}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
