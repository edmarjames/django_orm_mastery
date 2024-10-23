from django.apps import AppConfig
from django.db.models.signals import post_save


def example_receiver(sender, **kwargs):
    print("Instance is saved")

class InventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventory'

    def ready(self) -> None:
        post_save.connect(example_receiver)