from django.test import TestCase
from django.urls import reverse
from .views import home

class NavigationTests(TestCase):
    def test_home_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
