from django.apps import AppConfig


class KltnConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kltn'

#import send_email
    def ready(self):
        import kltn.signals  # Import signals.py
