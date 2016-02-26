from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Category


class CategoryDetailView(DetailView):
    """Return category detail."""
    template_name = 'categories/detail.html'
    model = Category
    context_object_name = 'category'


class CategoryListView(ListView):
    """Return category lists."""

    template_name = 'categories/list.html'
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'categories'
