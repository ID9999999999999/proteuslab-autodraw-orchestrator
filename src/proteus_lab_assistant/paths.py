from __future__ import annotations
from pathlib import Path

APP_DIR = Path.home() / ".proteus_lab_assistant"
DEFAULT_PROFILE = APP_DIR / "profile.json"
LOG_DIR = APP_DIR / "logs"

def ensure_app_dir() -> Path:
    APP_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    return APP_DIR

def desktop_path(filename: str) -> Path:
    return Path.home() / "Desktop" / filename
