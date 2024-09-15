from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.urls import reverse

class UserAuthTests(TestCase):

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123'
        })
        self.assertEqual(response.status_code, 302)  # assuming a redirect on success
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_user_login(self):
        User.objects.create_user(username='testuser', password='password')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 302)  # assuming a redirect on success
        self.assertRedirects(response, reverse('dharshana'))

    def test_user_logout(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
