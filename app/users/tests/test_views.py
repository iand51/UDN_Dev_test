from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestUserViews(TestCase):
    """
    Tests User app views
    """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
                    username='iand51',
                    password='password123',
                    email='idonlon@gmail.com')

    def test_login_view(self):
        """
        Test response code for login page
        """
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)

    def test_logout_view(self):
        """
        Tests response code for logout page and home page after logout
        """
        self.client.login(username='iand51', password='password123')
        self.client.logout()

        response = self.client.get(reverse('logout'))
        response2 = self.client.get(reverse('participant_home'))

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response2.status_code, 302)

    def test_form_view(self):
        """
        Test response code for views
        """
        response = self.client.get(reverse('participant_form'))
        self.assertEquals(response.status_code, 200)
