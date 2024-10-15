from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    # To set a verbose name for a field you can do this
    # name = models.CharField("brand_name", max_length=100)

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.name}"