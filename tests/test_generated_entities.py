"""The generated entities match the registry schemas in `data/entity`: running
bin/generate-entities.py again would change nothing."""

from __future__ import annotations

import filecmp
import importlib.util
import shutil
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent


def test_generated_code_is_up_to_date(tmp_path: Path) -> None:
    package_dir = ROOT_DIR / "src" / "syrtis_python_client"
    copy_root = tmp_path / "root"
    shutil.copytree(ROOT_DIR / "bin", copy_root / "bin")
    shutil.copytree(
        package_dir,
        copy_root / "src" / package_dir.name,
        ignore=shutil.ignore_patterns("__pycache__"),
    )

    spec = importlib.util.spec_from_file_location(
        "generate_entities", copy_root / "bin" / "generate-entities.py"
    )
    generator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(generator)
    assert generator.main() == 0

    stale = [
        str(path.relative_to(copy_root / "src"))
        for path in sorted((copy_root / "src").rglob("*.py"))
        if not filecmp.cmp(path, package_dir.parent / path.relative_to(copy_root / "src"), shallow=False)
    ]
    assert not stale, f"Regenerate the entities (bin/generate-entities.py): {stale}"
