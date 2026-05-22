from __future__ import annotations
import json
import shutil
from pathlib import Path
from typing import Any
from .models import Point
from .paths import DEFAULT_PROFILE, ensure_app_dir

class Profile:
    def __init__(self, data: dict[str, Any], path: Path | None = None) -> None:
        self.data = data
        self.path = path

    @classmethod
    def load(cls, path: str | Path | None = None) -> "Profile":
        p = Path(path) if path else DEFAULT_PROFILE
        if not p.exists():
            raise FileNotFoundError(f"Profile not found: {p}. Run: proteus-lab calibrate")
        return cls(json.loads(p.read_text(encoding="utf-8")), p)

    def save(self, path: str | Path | None = None) -> Path:
        p = Path(path) if path else DEFAULT_PROFILE
        ensure_app_dir()
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(self.data, indent=2, ensure_ascii=False), encoding="utf-8")
        self.path = p
        return p

    def export(self, output: str | Path) -> Path:
        if self.path is None:
            self.save()
        out = Path(output)
        shutil.copyfile(self.path or DEFAULT_PROFILE, out)
        return out

    @staticmethod
    def import_profile(input_path: str | Path) -> Path:
        ensure_app_dir()
        src = Path(input_path)
        if not src.exists():
            raise FileNotFoundError(src)
        shutil.copyfile(src, DEFAULT_PROFILE)
        return DEFAULT_PROFILE

    def point(self, dotted_key: str) -> Point:
        value: Any = self.data
        for key in dotted_key.split("."):
            value = value[key]
        return Point.from_dict(value)

    def actual_from_relative(self, rel: list[float]) -> Point:
        origin = self.point("schematic.origin")
        grid = float(self.data.get("schematic", {}).get("grid_step", 40))
        return Point(int(origin.x + float(rel[0]) * grid), int(origin.y + float(rel[1]) * grid))

def make_profile(points: dict[str, Point], grid_step: int = 40) -> Profile:
    return Profile({
        "version": 2,
        "proteus": {
            "pick_search_box": points["pick_search_box"].to_dict(),
            "pick_ok_button": points["pick_ok_button"].to_dict()
        },
        "schematic": {"origin": points["schematic_origin"].to_dict(), "grid_step": grid_step}
    })
