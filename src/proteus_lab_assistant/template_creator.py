from __future__ import annotations
import json
from pathlib import Path

def create_task_template(task_id: str, title: str, output: str | Path) -> Path:
    data = {
        task_id: {
            "title": title,
            "components": [{"name": "COMPONENT_NAME", "placements": [[0, 0]]}],
            "wires": [{"label": "wire_1", "points": [[0, 0], [1, 1]]}]
        }
    }
    out = Path(output)
    out.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return out
