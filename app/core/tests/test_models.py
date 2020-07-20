from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'mail@mail.com'
        password = 'Testpass123'
        user = get_user_model().objetcs.create_user(
            email=email,
            password=password
        )

        self.asserEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email for a new user is normalized"""
        email = 'test@BRASIL.COM'
        user = get_user_model().objetcs.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())