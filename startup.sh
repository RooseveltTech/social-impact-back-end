export LANG=C.UTF-8

celery -A social_app worker --loglevel=INFO --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo & celery -A social_app beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler & gunicorn --bind=0.0.0.0 social_app.wsgi