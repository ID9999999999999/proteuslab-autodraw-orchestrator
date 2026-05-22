from __future__ import annotations
import time
from pathlib import Path
from .models import Point
from .paths import desktop_path
from .safety import legal_notice, validate_project_filename

class GuiEngine:
    def __init__(self, dry_run: bool = False, interactive: bool = False, pause: float = 0.15) -> None:
        try:
            import pyautogui
        except ImportError as exc:
            raise RuntimeError("pyautogui is missing. Run: pip install -r requirements.txt") from exc
        self.pg = pyautogui
        self.pg.PAUSE = pause
        self.dry_run = dry_run
        self.interactive = interactive

    def _step(self, text: str) -> None:
        print(text)
        if self.interactive and not self.dry_run:
            input("Press Enter to execute...")

    def wait(self, seconds: float, note: str = "") -> None:
        self._step(f"WAIT {seconds}s {note}".strip())
        if not self.dry_run:
            time.sleep(seconds)

    def click(self, p: Point, note: str = "") -> None:
        self._step(f"CLICK ({p.x}, {p.y}) {note}".strip())
        if not self.dry_run:
            self.pg.click(p.x, p.y)

    def hotkey(self, *keys: str, note: str = "") -> None:
        self._step(f"HOTKEY {'+'.join(keys)} {note}".strip())
        if not self.dry_run:
            self.pg.hotkey(*keys)

    def press(self, key: str, note: str = "") -> None:
        self._step(f"PRESS {key} {note}".strip())
        if not self.dry_run:
            self.pg.press(key)

    def write_text(self, text: str, note: str = "") -> None:
        self._step(f"WRITE {text!r} {note}".strip())
        if not self.dry_run:
            self.pg.write(text, interval=0.01)

    def screenshot(self, output: str | Path) -> Path:
        out = Path(output)
        out.parent.mkdir(parents=True, exist_ok=True)
        self._step(f"SCREENSHOT -> {out}")
        if not self.dry_run:
            img = self.pg.screenshot()
            img.save(out)
        return out

    def current_position(self) -> Point:
        x, y = self.pg.position()
        return Point(int(x), int(y))

    def open_pick_devices(self, pick_button: Point) -> None:
        self.click(pick_button, "open Pick Devices")

    def pick_component(self, name: str, search_box: Point, ok_button: Point) -> None:
        self.click(search_box, f"search component {name}")
        self.hotkey("ctrl", "a")
        self.write_text(name)
        self.wait(0.4, "wait for search results")
        self.click(ok_button, "confirm component")

    def place_component(self, p: Point, name: str) -> None:
        self.click(p, f"place {name}")

    def wire(self, points: list[Point], label: str) -> None:
        self._step(f"WIRE {label} with {len(points)} clicks")
        for p in points:
            self.click(p, f"wire {label}")

    def save_to_desktop(self, filename: str) -> Path:
        filename = validate_project_filename(filename)
        out = desktop_path(filename)
        print(legal_notice())
        self.hotkey("ctrl", "s", note="ask Proteus to save")
        self.wait(1.0, "wait for Save dialog; Demo may block here")
        self.write_text(str(out), note="type Desktop save path")
        self.press("enter", note="confirm save")
        self.wait(1.0, "wait for Proteus")
        print(f"Requested save to: {out}")
        return out
