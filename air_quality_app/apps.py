from django.apps import AppConfig


class AirQualityAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'air_quality_app'

    def ready(self):
        import air_quality_app.signals 
        
