#!/usr/bin/env python
import os
import subprocess
import sys
from pathlib import Path


def _use_project_python():
    venv_python = Path(__file__).resolve().parent / ".venv" / "Scripts" / "python.exe"
    if not venv_python.exists() or Path(sys.executable).resolve() == venv_python.resolve():
        return
    raise SystemExit(subprocess.call([str(venv_python), *sys.argv]))


if __name__ == "__main__":
    _use_project_python()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
