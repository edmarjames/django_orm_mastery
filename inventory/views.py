from django.shortcuts import render
from django.http import HttpResponse

from .models import (
    Category,
    Product,
)
from .forms import CreateProductForm

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import MySqlLexer
from sqlparse import format


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