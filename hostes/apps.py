from django.apps import AppConfig


class HostesConfig(AppConfig):
    name = 'hostes'

    def ready(self):
        import hostes.signals
