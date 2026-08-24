"""Verify that the Mathematics Atlas and every chapter lineage label are current."""

from pathlib import Path
import subprocess
import sys


root = Path(__file__).parents[1]
subprocess.run(
    [sys.executable, str(root / "tools" / "build_mathematics_atlas.py"), "--check"],
    cwd=root,
    check=True,
)
