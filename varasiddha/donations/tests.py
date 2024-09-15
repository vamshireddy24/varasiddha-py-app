from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class DonationsViewTests(TestCase):

    def test_donations_view(self):
        response = self.client.get(reverse('donations'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Donations")
        self.assertTemplateUsed(response, 'donations/donations.html')

    def test_pdf_upload(self):
        with open('path/to/sample.pdf', 'rb') as pdf_file:
            response = self.client.post(reverse('donation_upload'), {'pdf_file': pdf_file})
        self.assertEqual(response.status_code, 302)  # assuming a redirect on success
        self.assertRedirects(response, reverse('donations'))