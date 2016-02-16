from django.test import TestCase
from ..models import Product, Category
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
# models test


class CategoryTest(TestCase):

    def create_category(self):
        name = 'category_test'
        User = get_user_model()
        user = User.objects.create(username="admin", password="admin")
        return Category.objects.create(name = name, created_by = user)

    def create_category_slug_uniqe(self):
        name = 'category_test'
        return Category.objects.create(name = name)

    def test_CategoryTest_create(self):
        category = self.create_category()
        category_slug_uniqe = self.create_category_slug_uniqe()
        self.assertTrue(isinstance(category, Category))
        self.assertEqual(category.__unicode__(), category.name)
        self.assertEqual(category.created_by.username, 'admin')
        self.assertRaises(category.name == category_slug_uniqe.name)


