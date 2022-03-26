from django.apps import AppConfig


class NotifyerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notifyer'

    def ready(self):
        import notifyer.signals