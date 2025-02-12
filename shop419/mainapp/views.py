from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product

from django.template import loader

# to help return HTTP response to the user for any given request 
from django.http import HttpResponse

# Create your views here.
def homeView(request):
    products = Product.objects.all()
    context = {
        'product_list' : products
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))

def aboutView(request):
    context = {
        'name' : "krishna",
        'students' : [
            "suraj",
            "shivani",
            "deepak"
        ],

    }
    template = loader.get_template('about.html')
    return HttpResponse(template.render(context, request))

def contactView(request):
    context = {
        
    }
    template = loader.get_template('about.html')
    return HttpResponse(template.render(context, request))