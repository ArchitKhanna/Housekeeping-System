from django.apps import AppConfig


class HkmanagerConfig(AppConfig):
    name = 'HKmanager'

    def ready(self):
        import HKmanager.signals
