from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class AdminSiteTest(TestCase):
    """Setup function"""

    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            email='admin@admin.com',
            password='adminpassword1234'
        )
        self.client.force_login(self.admin_user)
        self.user = User.objects.create_user(
            email='test@test.com',
            password='testpassword1234',
            name='Test user'
        )

    def test_users_list(self):
        """Test users list shows on admin users list page"""
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """Test user change page works correctly"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """Test create user page works correctly"""
        url = reverse('admin:core_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
