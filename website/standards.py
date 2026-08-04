import csv
from pathlib import Path

STANDARDS_FILE = Path(__file__).resolve().parent.parent / "data" / "standards.csv"

def get_standards():
    with STANDARDS_FILE.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))
