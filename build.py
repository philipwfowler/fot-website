import csv
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"

def read_csv(filename):
    with (ROOT / "data" / filename).open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    (DIST / "static").mkdir(parents=True)
    shutil.copy2(ROOT / "static" / "site.css", DIST / "static" / "site.css")

    environment = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html"]))
    context = {
        "pricing": read_csv("pricing.csv"),
        "additional_services": read_csv("additional_services.csv"),
        "standards": read_csv("standards.csv"),
    }
    for template_name, output_name in (("home.html", "index.html"), ("contact.html", "contact.html")):
        (DIST / output_name).write_text(environment.get_template(template_name).render(**context), encoding="utf-8")
    print(f"Built static site in {DIST}")

if __name__ == "__main__":
    main()
