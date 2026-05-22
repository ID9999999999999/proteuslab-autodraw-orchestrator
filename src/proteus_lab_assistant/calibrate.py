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
    title("Calibration wizard")
    print("Open Proteus first. Keep the window size and zoom stable.")
    engine = GuiEngine()
    points = {
        "pick_devices_button": _capture(engine, "Pick Devices button (P)"),
        "pick_search_box": _capture(engine, "Pick Devices search/keyword box"),
        "pick_ok_button": _capture(engine, "Pick Devices OK button"),
        "schematic_origin": _capture(engine, "clean schematic origin point")
    }
    grid_raw = input("Grid step in pixels [40]: ").strip()
    grid = int(grid_raw) if grid_raw else 40
    path = make_profile(points, grid).save()
    ok(f"Profile saved: {path}")
