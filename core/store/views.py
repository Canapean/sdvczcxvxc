from django.shortcuts import render
from . models import Product

from django.views import generic


class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    context_object_name = 'product'
