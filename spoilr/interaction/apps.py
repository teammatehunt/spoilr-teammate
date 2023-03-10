from django.apps import AppConfig

# Register hunt callbacks.
from . import callbacks


class SpoilrInteractionConfig(AppConfig):
    name = "spoilr.interaction"

    # Override the prefix for database model tables.
    label = "spoilr_interaction"

    def ready(self):
        # Connect the signal handlers registered in signals
        from . import signals
