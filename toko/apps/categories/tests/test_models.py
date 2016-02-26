from django.test import TestCase

from ..models import Category


class CategoryTest(TestCase):

    def test_get_absolute_url(self):
        category = Category.objects.create(name='Drinks')
        self.assertEqual('/categories/drinks', category.get_absolute_url())
