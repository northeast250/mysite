from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rango.models import Category
from rango.models import Page


def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}



    # context_dict = {'boldmessage':"Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['categories'] = category
    except Category.DoesNotExist:
        context_dict['categories'] = None
        context_dict['pages'] = None
        
    return render(request, 'rango/category.html', context_dict)

