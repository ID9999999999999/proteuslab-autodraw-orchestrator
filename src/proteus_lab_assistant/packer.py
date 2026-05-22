from __future__ import annotations
from pathlib import Path
import zipfile

def pack_submission(output: str | Path, include: list[str]) -> Path:
    out = Path(output)
    if out.exists():
        out.unlink()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for item in include:
            p = Path(item)
            if not p.exists():
                continue
            if p.is_file():
                z.write(p, p.name)
            else:
                for f in p.rglob("*"):
                    if f.is_file():
                        z.write(f, str(f.relative_to(p.parent)))
    return out
