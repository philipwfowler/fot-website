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

## Production

Set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False`, `DJANGO_ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, and the email variables in `.env.example`. Then run:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn config.wsgi:application
```

The included `Procfile` suits platforms such as Render or Railway. Use PostgreSQL and HTTPS for production.

## Checks

```bash
python manage.py check
python manage.py test
```
