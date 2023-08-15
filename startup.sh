export LANG=C.UTF-8

celery -A social_app worker -l INFO -B & celery -A social_app beat -l INFO -S django_celery_beat.schedulers:DatabaseScheduler & gunicorn --bind=0.0.0.0:8000 social_app.wsgi