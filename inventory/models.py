from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True)
    url = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    quantity = models.IntegerField()
    # To set a verbose name for a field you can do this
    # name = models.CharField("brand_name", max_length=100)

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.name}"