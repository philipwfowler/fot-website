# Fowler Optical Testing website

A small Django website for Fowler Optical Testing LLP. It presents services, standards, charges, requirements, and contact details, with a contact form that sends enquiries by email.

## Local installation

Requires Python 3.11+.

```bash
python3 -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/. Copy `.env.example` to `.env` and configure SMTP for real email; otherwise submissions are printed in the terminal.

## Updating prices

Edit [`data/pricing.csv`](data/pricing.csv) to change the main service prices. Keep the header row (`service,gbp,usd,eur`) and add one row per service. Prices are shown on the website when the next page request is made; no HTML or Python changes are required.

Optional add-ons are managed separately in [`data/additional_services.csv`](data/additional_services.csv), using the same columns. The current add-ons are impact resistance, solar blue light reducing labelling, and expedited 48-hour reporting.

## Production

Set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False`, `DJANGO_ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, and the email variables in `.env.example`. Then run:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn config.wsgi:application
```

## Deploy to Render

The repository includes [`render.yaml`](render.yaml), which defines a Python web service and PostgreSQL database. Render recommends this Blueprint approach for Django deployments, with static files collected during the build and database migrations run before the service starts. See the [Render Django deployment guide](https://render.com/docs/deploy-django).

1. Push this repository to GitHub, GitLab, or Bitbucket.
2. In Render, choose **New → Blueprint** and connect the repository.
3. Apply the Blueprint. Render will create the web service and database, generate the Django secret key, install dependencies, collect static files, and run migrations.
4. In the web service’s Environment settings, enter the SMTP values for `EMAIL_HOST`, `EMAIL_HOST_USER`, and `EMAIL_HOST_PASSWORD`.
5. Add your final custom domain to `DJANGO_ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS`, then configure that domain in Render.

The Blueprint uses the placeholder hostname `fowler-optical-testing.onrender.com`; if Render assigns a different hostname, update those two environment variables before using the service. The contact form is deliberately not active for real delivery until SMTP credentials are configured.

Use PostgreSQL and HTTPS for production. SQLite remains the convenient default for local development.

## Checks

```bash
python manage.py check
python manage.py test
```
