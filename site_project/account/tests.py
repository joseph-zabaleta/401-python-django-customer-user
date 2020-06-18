from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from .models import CustomUser

class AccountTests(TestCase):
    

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'Debugger',
            email = 'debug@email.com',
            password = 'uncommon',
        )
    
    def test_creation(self):
        self.assertIsInstance(self.user, CustomUser)
        self.assertEqual(self.user.email, 'debug@email.com')
        self.assertIsNotNone(self.user.password)
        self.assertNotEqual(self.user.password, 'uncommon')
    
    def test_unique_email(self):
        try:
            fake_user = get_user_model().objects.create_user(
                username = 'Faker',
                email = 'debug@email.com',
                password = 'uncommon',
            )
        except IntegrityError:
            pass

        else:
            self.fail('ERROR: You attempted to created an account with an existing email!')