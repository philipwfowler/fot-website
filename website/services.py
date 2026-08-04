import csv
from pathlib import Path

SERVICES_FILE = Path(__file__).resolve().parent.parent / "data" / "additional_services.csv"

def get_additional_services():
    with SERVICES_FILE.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))
