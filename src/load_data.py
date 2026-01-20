"""Load raw data exports and print a quick inventory summary.

Run:
    python -m src.load_data
"""
from __future__ import annotations

import pathlib
import pandas as pd

RAW_DIR = pathlib.Path(__file__).resolve().parents[1] / "data_raw"

def _read_csv(path: pathlib.Path) -> pd.DataFrame:
    # Try common delimiters/encodings used in German exports.
    for sep in [",", ";", "\t"]:
        try:
            df = pd.read_csv(path, sep=sep, encoding="utf-8")
            if df.shape[1] > 1:
                return df
        except Exception:
            pass
    # Fallback
    return pd.read_csv(path, encoding="utf-8", engine="python")

def main() -> None:
    if not RAW_DIR.exists():
        raise SystemExit(f"Missing folder: {RAW_DIR}")
    files = sorted([p for p in RAW_DIR.iterdir() if p.suffix.lower() in {".csv", ".xlsx"}])
    if not files:
        print(f"No files found in {RAW_DIR}. Put your exports there.")
        return

    print("== Raw data inventory ==")
    for p in files:
        print(f"\n-- {p.name} --")
        if p.suffix.lower() == ".csv":
            df = _read_csv(p)
        else:
            df = pd.read_excel(p)
        print(f"shape: {df.shape}")
        print("columns:", list(df.columns))
        # missingness quick view
        miss = (df.isna().mean().sort_values(ascending=False) * 100).round(1)
        print("top missingness (%):")
        print(miss.head(10).to_string())

if __name__ == "__main__":
    main()
