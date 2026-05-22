from __future__ import annotations
from .engine import GuiEngine
from .models import Point
from .profile import Profile
from .tasks import get_task

class AutoDrawer:
    def __init__(self, engine: GuiEngine, profile: Profile) -> None:
        self.engine = engine
        self.profile = profile

    def _point(self, rel: list[float]) -> Point:
        return self.profile.actual_from_relative(rel)

    def draw_task(self, task_id: str) -> None:
        task = get_task(task_id)
        proteus = self.profile.data["proteus"]
        pick_button = Point.from_dict(proteus["pick_devices_button"])
        search_box = Point.from_dict(proteus["pick_search_box"])
        ok_button = Point.from_dict(proteus["pick_ok_button"])

        for component in task.get("components", []):
            name = component["name"]
            placements = component.get("placements", [])
            self.engine.open_pick_devices(pick_button)
            self.engine.pick_component(name, search_box, ok_button)
            for rel in placements:
                self.engine.place_component(self._point(rel), name)

        for wire in task.get("wires", []):
            label = wire["label"]
            points = [self._point(rel) for rel in wire["points"]]
            self.engine.wire(points, label)

        self.engine.screenshot(f"screenshots/{task_id}_drawn.png")

def draw_and_save(task_id: str, profile: Profile, filename: str, dry_run: bool = False, interactive: bool = False) -> None:
    engine = GuiEngine(dry_run=dry_run, interactive=interactive)
    drawer = AutoDrawer(engine, profile)
    drawer.draw_task(task_id)
    engine.save_to_desktop(filename)
