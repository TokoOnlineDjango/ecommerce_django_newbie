from django.core.exceptions import ValidationError
from django.test import TestCase

from toko.core.validators import validate_mobile_phone


class ValidatorTest(TestCase):
    def test_validate_mobile_phone(self):
        self.assertTrue(validate_mobile_phone('087782357971'))
        self.assertTrue(validate_mobile_phone('+6287788800124'))
        self.assertRaises(ValidationError, validate_mobile_phone, '35644522335')
