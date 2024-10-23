from django.http import HttpResponse
from django.shortcuts import render
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import MySqlLexer
from sqlparse import format

from .forms import CreateProductForm, CreateStockForm
from .models import Category, Product, Stock


# Create your views here.
def get_categories(request):

    all_category = Category.objects.all()
    sql_formatted = format(str(all_category.query), reindent=True)
    print(highlight(sql_formatted, MySqlLexer(), TerminalFormatter()))

    return HttpResponse(all_category.query)

def create_product(request):
    # create() is often use together with a form

    all_category = Category.objects.all()
    message = ""

    if request.method == "POST":
        form = CreateProductForm(request.POST)

        if form.is_valid() == True:
            form_data = form.cleaned_data
            try:
                category = Category.objects.get(name=form_data["categories"])

                Product.objects.create(
                    name = form_data["name"],
                    price = form_data["price"],
                    url = form_data["url"],
                    quantity = form_data["quantity"],
                    category = category
                )
                message = "Product successfully created!"
                # Alternative approach using save()
                # product = Product(
                #     name = form_data["name"],
                #     price = form_data["price"],
                #     url = form_data["url"],
                #     quantity = form_data["quantity"],
                #     category = category
                # )
                # product.save()
                # note: save() method can also be used when updating a record
            except Category.DoesNotExist:
                message = "Category does not exist"
            except Exception as e:
                message = f"An error occurred: {str(e)}"
        else:
            message = "Form is invalid. Please correct the errors."
    else:
        form = CreateProductForm()

    context = {
        "form": form,
        "all_category": all_category,
        "message": message
    }

    return render(request, "create_product.html", context)

def create_stock(request):

    all_product = Product.objects.all()
    all_stock = Stock.objects.all()
    message = ""

    if request.method == "POST":
        form = CreateStockForm(request.POST)

        if form.is_valid() == True:
            try:
                product = Product.objects.get(name=form.cleaned_data["product"])

                Stock.objects.create(
                    units = form.cleaned_data["units"],
                    product = product
                )
                message = "Stock created successfully!"
            except Product.DoesNotExist:
                message = "Product does not exist"
            except Exception as e:
                message = f"An error occurred {str(e)}"
        else:
            message = "Form is invalid. Please correct the errors."
    else:
        form = CreateStockForm()

    context = {
        "form": form,
        "all_product": all_product,
        "all_stock": all_stock,
        "message": message
    }

    return render(request, "create_stock.html", context)