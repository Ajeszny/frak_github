from django.apps import AppConfig


class AuthSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_system'
class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'your_app_name'

    def ready(self):
        import your_app_name.signals
