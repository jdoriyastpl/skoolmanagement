from django.apps import AppConfig


class SectionConfig(AppConfig):
    name = 'section'

    def ready(self):
        import section.receivers
