# Fowler Optical Testing website

A lightweight static website for Fowler Optical Testing LLP. Python and Jinja2 build the HTML from the CSV data files; Render serves the generated `dist/` directory as a free Static Site.

## Local installation

Requires Python 3.11+.

```bash
python3 -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python build.py
```

Open `dist/index.html` in a browser, or serve it locally with:

```bash
python3 -m http.server 8000 --directory dist
```

## Updating content

- [`data/pricing.csv`](data/pricing.csv) contains the main per-style prices.
- [`data/additional_services.csv`](data/additional_services.csv) contains optional add-ons.
- [`data/standards.csv`](data/standards.csv) contains standard names, descriptions, sections, and URLs.

Run `python build.py` after changing a CSV file. The generated files in `dist/` are deployment output and are ignored by Git.

## Deploy to Render for free

The included [`render.yaml`](render.yaml) defines a Render Static Site. Push the repository to GitHub, GitLab, or Bitbucket, then choose **New → Blueprint** in Render and connect the repository. Render will run the build command and publish `dist/`.

The same setup can be created manually as **New → Static Site**:

```text
Build command: ./build-static.sh
Publish directory: dist
```

Render’s Static Sites are free and receive automatic deploys when the configured Git branch changes. See the [Render Static Sites documentation](https://render.com/docs/static-sites).

## Contact

The site uses a `mailto:` link to `query@fowleropticaltesting.co.uk`. Clicking “Email Fowler Optical Testing” opens the visitor’s email application; no server or form-processing service is required.
