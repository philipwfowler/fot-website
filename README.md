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

The included [`render.yaml`](render.yaml) defines a Render Static Site. No database, server, or environment variables are required.

### Option 1: Use the Blueprint

1. Create an empty repository on GitHub, GitLab, or Bitbucket.
2. From this project directory, commit and push the code:

   ```bash
   git remote add origin YOUR_REPOSITORY_URL
   git push -u origin main
   ```

   If an `origin` remote already exists, use `git push -u origin main` only.
3. Sign in to [Render](https://dashboard.render.com/).
4. Choose **New → Blueprint**.
5. Connect the repository and select the `main` branch.
6. Review the Blueprint, then choose **Apply**.

Render will run `./build-static.sh`, install Jinja2, generate the HTML in `dist/`, and publish that directory. It will automatically redeploy when new commits are pushed to `main`.

### Option 2: Create the Static Site manually

Choose **New → Static Site**, connect the repository, and use the `main` branch. Enter:

```text
Build command: ./build-static.sh
Publish directory: dist
```

Leave the environment-variable section empty, then create the site.

After the first deploy, Render provides an `onrender.com` URL. A custom domain can be added from the site’s **Settings → Custom Domains** page.

Render’s Static Sites are free and receive automatic deploys when the configured Git branch changes. See the [Render Static Sites documentation](https://render.com/docs/static-sites).

## Contact

The site uses a `mailto:` link to `query@fowleropticaltesting.co.uk`. Clicking “Email Fowler Optical Testing” opens the visitor’s email application; no server or form-processing service is required.
