from django.apps import AppConfig

class AuthenticationConfig(AppConfig):
    name = 'apps.cuenta'

    def ready(self):
        import apps.cuenta.signals