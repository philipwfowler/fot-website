import csv
from pathlib import Path

PRICING_FILE = Path(__file__).resolve().parent.parent / "data" / "pricing.csv"

def get_pricing():
    """Return the current pricing rows from the editable CSV file."""
    with PRICING_FILE.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))
