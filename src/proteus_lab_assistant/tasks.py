from __future__ import annotations
import json
from importlib.resources import files
from typing import Any

def load_tasks() -> dict[str, Any]:
    data_path = files("proteus_lab_assistant.data").joinpath("tasks.json")
    return json.loads(data_path.read_text(encoding="utf-8"))

def available_tasks() -> dict[str, str]:
    return {key: value["title"] for key, value in load_tasks()["tasks"].items()}

def get_task(task_id: str) -> dict[str, Any]:
    tasks = load_tasks()["tasks"]
    if task_id not in tasks:
        raise ValueError(f"Unknown task: {task_id}. Available: {', '.join(sorted(tasks))}")
    return tasks[task_id]
