from django.apps import AppConfig


class SpoilrCoreConfig(AppConfig):
    name = "spoilr.core"

    # Override the prefix for database model tables.
    label = "spoilr_core"

    def ready(self):
        # Connect the signal handlers registered in signals
        from . import signals
