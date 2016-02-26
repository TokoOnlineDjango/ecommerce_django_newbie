from django.core.files import File
from django.test import TestCase

from toko.apps.users.models import User
from toko.apps.categories.models import Category

from ..models import Product


class ProductTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='kangfend', password='test123')
        self.category = Category.objects.create(name='Drink')
        self.data = {
            'name': 'Product 1',
            'description': 'Product description',
            'is_active': True,
            'price': 100000
        }
        self.product = self.user.products.create(**self.data)
        self.product.categories.add(self.category)

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

    def test_get_absolute_url(self):
        # Ensure get_absolute_url return a valid url
        self.assertEqual(self.product.get_absolute_url(),
                         '/products/%s' % self.product.slug)

    def test_get_related_product(self):
        product_1 = self.product

        self.data['name'] = 'Buavita'
        product_2 = self.user.products.create(**self.data)
        product_2.categories.add(self.category)

        self.data['name'] = 'Asus Zenfone 5'
        category = self.user.categories.create(name='Smartphone')
        product_3 = self.user.products.create(**self.data)
        product_3.categories.add(category)
        self.assertIn(product_2, product_1.get_related())
        self.assertIn(product_1, product_2.get_related())
        self.assertNotIn(product_3, product_1.get_related())
        self.assertNotIn(product_3, product_2.get_related())
        self.assertNotIn(product_1, product_3.get_related())
        self.assertNotIn(product_2, product_3.get_related())

    def test_active_queryset(self):
        product_1 = self.product
        self.data['is_active'] = False
        product_2 = self.user.products.create(**self.data)
        result = Product.objects.active()
        self.assertIn(product_1, result)
        self.assertNotIn(product_2, result)

    def test_featured_queryset(self):
        product_1 = self.product
        self.data['is_featured'] = True
        product_2 = self.user.products.create(**self.data)
        result = Product.objects.featured()
        self.assertIn(product_2, result)
        self.assertNotIn(product_1, result)

    def test_primary_image(self):
        # Test primary image if product has no image
        self.assertEqual(self.product.primary_image, None)

        # Upload product image 1
        with File(open('toko/static/images/favicon.ico')) as image:
            image_1 = self.product.photos.create(image=image)

        # Upload product image 2
        with File(open('toko/static/images/favicon.ico')) as image:
            image_2 = self.product.photos.create(image=image)

        # Ensure this method return the first image
        self.assertEqual(self.product.primary_image, image_1.image)
        self.assertNotEqual(self.product.primary_image, image_2.image)
