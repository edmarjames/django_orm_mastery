from django.urls import path
from . import views

app_name = "inventory"

urlpatterns = [
    path('', views.get_categories, name="get_categories"),
    path('create_product', views.create_product, name="create_product"),
]
