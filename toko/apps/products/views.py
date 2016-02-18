from operator import __or__ as OR

from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Product, Category


class CategoryDetailView(DetailView):
    """Return category detail."""

    template_name = 'categories/detail.html'
    model = Category
    context_object_name = 'object_category'


class CategoryListView(ListView):
    """Return category lists."""

    template_name = 'categories/list.html'
    model = Category
    queryset = Category.objects.all()

    context_object_name = 'categories'


class ProductDetailView(DetailView):
    """Return product detail."""

    template_name = 'products/detail.html'
    model = Product
    context_object_name = 'product'


class ProductListlView(ListView):
    """Return product list."""

    template_name = 'products/list.html'
    model = Product
    queryset = Product.objects.all()

    context_object_name = 'products'

    def get_queryset(self, *arg, **kwargs):
        """Return query search."""
        queryset = super(ProductListlView, self).get_queryset(*arg, **kwargs)
        query = self.request.GET.get('q')
        if query:
            q_objects = [Q(name__icontains=query), Q(description__icontains=query)]
            if query.isdigit():
                q_objects.append(Q(price=query))
            queryset = queryset.filter(reduce(OR, q_objects))
        return queryset
