"""Build a merged SSOT dataset (placeholder).

This will later merge CRM deals + activities + revenue + marketing sources.
For now, it simply concatenates cleaned tables into a single 'catalog' for exploration.

Run:
    python -m src.build_ssot
"""
from __future__ import annotations

import pathlib
import pandas as pd

CLEAN_DIR = pathlib.Path(__file__).resolve().parents[1] / "data_clean"
OUT_DIR = pathlib.Path(__file__).resolve().parents[1] / "data_clean"

def main() -> None:
    files = sorted([p for p in CLEAN_DIR.iterdir() if p.name.endswith("_clean.csv")])
    if not files:
        print("No cleaned files. Run: python -m src.clean")
        return

    catalog = []
    for p in files:
        df = pd.read_csv(p)
        df.insert(0, "source_file", p.name)
        catalog.append(df)

    merged = pd.concat(catalog, ignore_index=True, sort=False)
    out = OUT_DIR / "ssot_catalog.csv"
    merged.to_csv(out, index=False)
    print(f"Wrote {out} with {merged.shape[0]} rows and {merged.shape[1]} cols")

if __name__ == "__main__":
    main()
