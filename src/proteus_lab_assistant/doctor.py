from __future__ import annotations
import platform
import sys
from pathlib import Path
from .console import ok, warn, title
from .paths import DEFAULT_PROFILE

def run_doctor() -> int:
    title("Proteus Lab Assistant doctor")
    print(f"Python: {sys.version.split()[0]}")
    print(f"OS: {platform.system()} {platform.release()}")
    try:
        import pyautogui  # noqa
        ok("pyautogui installed")
    except Exception as exc:
        warn(f"pyautogui problem: {exc}")
        return 1
    desktop = Path.home() / "Desktop"
    ok(f"Desktop path: {desktop}") if desktop.exists() else warn(f"Desktop not found: {desktop}")
    ok(f"Profile found: {DEFAULT_PROFILE}") if DEFAULT_PROFILE.exists() else warn("No profile yet. Run: proteus-lab calibrate")
    print("Reminder: saving works only if Proteus itself allows saving.")
    return 0
