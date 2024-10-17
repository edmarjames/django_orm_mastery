from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True)
    url = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    # To set a verbose name for a field you can do this
    # name = models.CharField("brand_name", max_length=100)

    # To create a many to many field you can do this, create a many to many field will create a link table
    # category = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.name} - {self.category.name}"

class Brand(models.Model):
    # You can explicitly define your primary key like this. See example below.
    # brand_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.name}"

class Stock(models.Model):
    units = models.BigIntegerField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} - {self.units}"
