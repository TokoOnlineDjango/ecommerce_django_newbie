from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from ..models import Product


class CategoryViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(**{
            'name': 'Product 1',
            'description': 'Product description',
            'is_active': True,
            'price': 100000
        })

    def test_detail_category(self):
        response = self.client.get(reverse(
            'products:detail', args=[self.product.slug]))
        self.assertEqual(response.status_code, 200)

    def test_list_category(self):
        response = self.client.get(reverse('products:list'))
        self.assertEqual(response.status_code, 200)
