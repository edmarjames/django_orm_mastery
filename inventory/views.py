from django.shortcuts import render
from django.http import HttpResponse

from .models import Category

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