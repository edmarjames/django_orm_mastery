from django import forms

class CreateProductForm(forms.Form):
    name = forms.CharField(label="name", max_length=100)
    price = forms.DecimalField(label="price", max_digits=10, decimal_places=2)
    url = forms.SlugField(label="url")
    quantity = forms.IntegerField(label="quantity", max_value=50)
    categories = forms.CharField(label="categories", max_length=255)
