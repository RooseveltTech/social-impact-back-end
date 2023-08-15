export LANG=C.UTF-8

gunicorn — bind=0.0.0.0 — timeout 600 social_app.wsgi & celery -A social_app worker -l INFO -B