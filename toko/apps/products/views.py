from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Product

class ProductDetailView(DetailView):
    template_name = 'products/detail.html'
    model = Product
    context_object_name = 'product'

class ProductListlView(ListView):
    template_name = 'products/list.html'
    model = Product
    queryset = Product.objects.all()

    context_object_name = 'products'
