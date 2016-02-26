from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from ..models import Category


class CategoryViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_detail_category(self):
        category = Category.objects.create(name='Drinks')
        response = self.client.get(reverse(
            'categories:detail', args=[category.slug]))
        self.assertEqual(response.status_code, 200)

    def test_list_category(self):
        response = self.client.get(reverse('categories:list'))
        self.assertEqual(response.status_code, 200)
