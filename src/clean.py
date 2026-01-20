"""Clean and standardize raw exports into data_clean/.

Run:
    python -m src.clean
"""
from __future__ import annotations

import pathlib
import re
import pandas as pd

RAW_DIR = pathlib.Path(__file__).resolve().parents[1] / "data_raw"
CLEAN_DIR = pathlib.Path(__file__).resolve().parents[1] / "data_clean"

def snake_case(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^0-9a-zA-Z]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s

def read_csv_flexible(path: pathlib.Path) -> pd.DataFrame:
    for sep in [",", ";", "\t"]:
        try:
            df = pd.read_csv(path, sep=sep, encoding="utf-8")
            if df.shape[1] > 1:
                return df
        except Exception:
            pass
    return pd.read_csv(path, encoding="utf-8", engine="python")

def main() -> None:
    CLEAN_DIR.mkdir(exist_ok=True)
    files = sorted([p for p in RAW_DIR.iterdir() if p.suffix.lower() in {".csv", ".xlsx"}])
    if not files:
        print("No raw files. Put exports into data_raw/.")
        return

    for p in files:
        if p.suffix.lower() == ".csv":
            df = read_csv_flexible(p)
        else:
            df = pd.read_excel(p)

        df.columns = [snake_case(c) for c in df.columns]
        out = CLEAN_DIR / (p.stem + "_clean.csv")
        df.to_csv(out, index=False)
        print(f"Wrote {out.name} ({df.shape[0]} rows)")

if __name__ == "__main__":
    main()
