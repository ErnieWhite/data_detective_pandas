from __future__ import annotations
from pathlib import Path
import textwrap
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

def banner(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)
