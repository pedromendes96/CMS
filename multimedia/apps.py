from django.apps import AppConfig


class MultimediaConfig(AppConfig):
    name = 'multimedia'

    def ready(self):
        from multimedia import signals
