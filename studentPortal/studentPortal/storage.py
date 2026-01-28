from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path

DELIM = "|"

@dataclass
class Storage:
    base_dir: Path

    def path(self, filename: str) -> Path:
        p = self.base_dir / filename
        p.parent.mkdir(parents=True, exist_ok=True)
        if not p.exists():
            p.write_text("", encoding="utf-8")
        return p

    def read_rows(self, filename: str) -> list[list[str]]:
        p = self.path(filename)
        lines = [ln.strip() for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]
        return [ln.split(DELIM) for ln in lines]

    def write_rows(self, filename: str, rows: list[list[str]]) -> None:
        p = self.path(filename)
        text = "\n".join(DELIM.join(map(str, r)) for r in rows)
        p.write_text(text + ("\n" if text else ""), encoding="utf-8")
