from unittest import result
from django.shortcuts import render
from .models import Product



# importing url resoution tools
from django.urls import reverse, reverse_lazy


# to help to load template file
from django.template import loader

# to help return HTTP response to the user for any given request 
from django.http import HttpResponse

# importing the generic calss based viwes for CRUD operations

from django.views.generic import CreateView, DeleteView, UpdateView, DeleteView

# Create your views here.
def homeView(request):
    products = Product.objects.all()
    context = {
        'product_list' : products,
        'current_page' : 'home'
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))

def aboutView(request):
    context = {
        'current_page' : 'about'
    }
    template = loader.get_template('about.html')
    return HttpResponse(template.render(context, request))

def contactsView(request):
    context = {
        'current_page' : 'view'
    }
    template = loader.get_template('contacts.html')
    return HttpResponse(template.render(context, request))

class AddProduct(CreateView):
    model = Product
    fields = ['name', 'price', 'desc', 'pic', 'stock']
    template_name = 'addproduct.html'
    success_url = reverse_lazy('home')

# read -> show details of each product
class ProductDetails(DeleteView):
    model = Product
    template_name = 'prod_details.html'
    context_object_name = 'prod'

# update ->
class UpdateProduct(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'editProduct.html'


    def det_success_url(self):
        return reverse('prod_details', kwargs = {'pk' : self.object.pk})

# Delete
class DeleteProduct(DeleteView):
    model = Product
    template_name = 'delproduct.html'
    success_url = reverse_lazy('homepage')

# search result
def searchView(request):
    query=request.GET.get('search_text')
    #fetch the query text from GET request

    result = Product.objects.filter(name__icontains = query)
    #collect the product object matching the name 
    #this runs 'SELECT' * FROM product WHERE name like '%<query>%';
    #icontains is case-insenitive
    #contains can be used for case-sensitive

    context = {
        'items'  : result,
        'query' : query
    }
    template = loader.get_template('searchResults.html')
    return HttpResponse(template.render(context,request))