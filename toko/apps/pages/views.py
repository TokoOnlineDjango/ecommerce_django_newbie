from django.views.generic import TemplateView
from toko.apps.products.models import ProductFeatured


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['featured'] = ProductFeatured.objects.first()
        return context
