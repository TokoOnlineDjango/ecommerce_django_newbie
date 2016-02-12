from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Product

class ProductDetailView(DetailView):
    model = Product

class ProductListlView(ListView):
    model = Product
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductListlView, self).get_context_data(**kwargs)
        return context
