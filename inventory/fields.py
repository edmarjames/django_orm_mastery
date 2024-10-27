from django.db import models

class ProductDescriptionField(models.TextField):

    description = "Product description"

    def __init__(self, *args, **kwargs):
        kwargs["default"] = "Test description"
        kwargs["help_text"] = "Describe your product"
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value is None:
            return None
        return value.upper()

    def from_db_value(self, value, expression, connection):
        if value is None:
            return None
        return value.lower()