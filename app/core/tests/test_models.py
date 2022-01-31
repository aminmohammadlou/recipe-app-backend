from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class ModelTests(TestCase):
    """Test creating a new user"""
    def test_create_user_with_email(self):
        email = 'test@test.com'
        password = 'testpassword1234'
        user = User.objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email of new user to be normalized"""
        email = 'test@TEST.COM'
        user = User.objects.create_user(
            email=email,
            password='testpassword1234'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating a new user with no email raises an error"""
        with self.assertRaises(ValueError):
            User.objects.create_user(None, 'testpassword1234')

    def test_create_new_superuser(self):
        """Test creating new superuser"""
        user = User.objects.create_superuser(
            email='test@test.com',
            password='testpassword1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
