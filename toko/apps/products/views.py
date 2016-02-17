from django.db.models import Q
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

    def get_queryset(self, *arg, **kwargs):
        queryset = super(ProductListlView, self).get_queryset(*arg, **kwargs)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(name__icontains=query) |
                                       Q(description__icontains=query))
            try:
                search_price = queryset.filter(Q(price=query))
                queryset = (search_price | queryset).distinct()
            except Exception:
                pass
        return queryset
