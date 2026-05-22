from __future__ import annotations
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Point":
        return cls(x=int(data["x"]), y=int(data["y"]))

    def to_dict(self) -> dict[str, int]:
        return {"x": self.x, "y": self.y}
