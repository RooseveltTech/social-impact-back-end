export LANG=C.UTF-8

gunicorn --bind=0.0.0.0 social_app.wsgi & celery -A social_app worker --loglevel=INFO --pool=solo & celery -A social_app beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler