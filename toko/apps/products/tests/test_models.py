from django.test import TestCase

from ..models import Category, Product
from toko.apps.users.models import User


class ProductTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='kangfend', password='test123')
        self.category = Category.objects.create(name='Drink')
        self.product = Product.objects.create(name='Pepsi')
        # self.products.categories.add(categories= self.category)
        self.data = {
            'name': 'Product 1',
            'description': 'Product description',
            'is_active': True,
            'categories': self.products.categories.add(self.category),
            'price': 100000
        }
        self.product = self.user.products.create(**self.data)

    def test_product_manager(self):
        product_1 = self.product

        # Create product 2
        self.data['name'] = 'Product 2'
        product_2 = self.user.products.create(**self.data)

        # Create product 3
        self.data['name'] = 'Product 3'
        self.data['is_active'] = False
        product_3 = self.user.products.create(**self.data)

        # This query should return all product with status active
        products = Product.objects.all()
        self.assertIn(product_1, products)
        self.assertIn(product_2, products)
        self.assertNotIn(product_3, products)

    def test_product_method(self):
        # Ensure get_absolute_url return a valid url
        self.assertEqual(self.product.get_absolute_url(),
                         '/products/%s/detail' % self.product.id)