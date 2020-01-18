from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestClientViews(TestCase):
    """
    Tests the client app view
    """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
                    username='iand51',
                    password='password123',
                    email='idonlon@gmail.com')

    def test_home_redirect(self):
        """
        Test that home page redirects when not logged in
        """
        response = self.client.get(reverse('participant_home'))
        self.assertEquals(response.status_code, 302)

    def test_home_GET(self):
        """
        Test that homepage is avaliable after login
        """
        self.client.login(username='iand51', password='password123')
        response = self.client.get(reverse('participant_home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'client/home.html')
