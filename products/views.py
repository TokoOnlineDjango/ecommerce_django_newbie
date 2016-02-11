from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.
from .models import Product


class ProductDetailView(DetailView):
    model = Product

class ProductListlView(ListView):
    model = Product
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        contex = super(ProductListlView, self).get_context_data(**kwargs)
        print contex
        return contex




def product_detail_view_function(request, id):
    priduct_instance = Product.objects.get(id=id)
    template = 'products/product_detail.html'
    context = {
        'object':priduct_instance
    }
    return render(request, template, context)
