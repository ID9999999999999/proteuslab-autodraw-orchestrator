from __future__ import annotations

def title(text: str) -> None:
    print()
    print("=" * len(text))
    print(text)
    print("=" * len(text))

def ok(text: str) -> None:
    print(f"[OK] {text}")

def warn(text: str) -> None:
    print(f"[WARNING] {text}")

def ask_yes_no(prompt: str, default: bool = True) -> bool:
    suffix = "[Y/n]" if default else "[y/N]"
    raw = input(f"{prompt} {suffix}: ").strip().lower()
    if not raw:
        return default
    return raw in {"y", "yes", "1", "true"}
