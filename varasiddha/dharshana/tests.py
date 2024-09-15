from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class DharshanaViewTests(TestCase):

    def test_dharshana_view_requires_login(self):
        response = self.client.get(reverse('dharshana'))
        self.assertRedirects(response, '/accounts/login/?next=/dharshana/')

    def test_dharshana_view_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('dharshana'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dharshana")
        self.assertTemplateUsed(response, 'dharshana/dharshana.html')
