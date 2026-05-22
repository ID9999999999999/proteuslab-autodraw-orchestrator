from __future__ import annotations
from .console import title, ok
from .engine import GuiEngine
from .models import Point
from .profile import make_profile


def _capture(engine: GuiEngine, name: str) -> Point:
    print()
    print(f"Move your mouse to: {name}")
    input("Press Enter here when ready...")
    p = engine.current_position()
    ok(f"{name}: x={p.x}, y={p.y}")
    return p


def run_calibration() -> None:
    title("Simple Calibration Wizard")
    print("This simplified calibration does NOT ask for the Pick Devices P button.")
    print()
    print("Before continuing:")
    print("1. Open Proteus.")
    print("2. Open a blank schematic page.")
    print("3. Open the Pick Devices window manually by pressing P or clicking the P button.")
    print("4. Keep the Pick Devices window visible.")
    input("Press Enter here only after the Pick Devices window is open...")

    engine = GuiEngine()

    points = {
        "pick_search_box": _capture(engine, "Pick Devices search/keyword box"),
        "pick_ok_button": _capture(engine, "Pick Devices OK button"),
    }

    print()
    print("Now close the Pick Devices window manually and return to the blank schematic page.")
    print("Choose a clean empty point on the schematic. This will become the drawing origin.")
    input("Press Enter here after the Pick Devices window is closed...")

    points["schematic_origin"] = _capture(engine, "clean schematic origin point")

    grid_raw = input("Grid step in pixels [40]: ").strip()
    grid = int(grid_raw) if grid_raw else 40
    path = make_profile(points, grid).save()
    ok(f"Profile saved: {path}")
    print()
    print("Next safe test:")
    print("proteus-lab auto --task task1_xnor --filename Lab3_Task1_XNOR.pdsprj --dry-run")
