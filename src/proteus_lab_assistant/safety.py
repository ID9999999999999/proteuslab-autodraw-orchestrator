from __future__ import annotations

BANNED_GOALS = ["crack", "bypass license", "remove demo limitation", "fake pdsprj", "generate fake .pdsprj", "forge proteus", "keygen", "serial"]

def legal_notice() -> str:
    return "This assistant controls the real Proteus GUI only. It cannot bypass license restrictions and never creates fake .pdsprj files."

def assert_safe_text(text: str) -> None:
    lowered = text.lower()
    for banned in BANNED_GOALS:
        if banned in lowered:
            raise ValueError("Refused: unsafe or illegal goal.")

def validate_project_filename(filename: str) -> str:
    filename = filename.strip()
    if not filename:
        raise ValueError("Filename cannot be empty.")
    if "/" in filename or "\\" in filename:
        raise ValueError("Use only a filename, not a full path. The tool saves to Desktop.")
    if not (filename.endswith(".pdsprj") or filename.endswith(".dsn")):
        raise ValueError("Filename must end with .pdsprj or .dsn")
    for char in ['<', '>', ':', '"', '|', '?', '*']:
        if char in filename:
            raise ValueError(f"Invalid filename character: {char}")
    return filename
