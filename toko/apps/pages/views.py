from django.views.generic import TemplateView
from toko.apps.products.models import Product


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['featured_products'] = Product.objects \
            .prefetch_related('photos').featured()
        return context
