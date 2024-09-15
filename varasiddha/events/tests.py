from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class EventsViewTests(TestCase):

    def test_events_view(self):
        response = self.client.get(reverse('events'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Events")
        self.assertTemplateUsed(response, 'events/events.html')

    def test_create_event(self):
        response = self.client.post(reverse('event_create'), {
            'name': 'Sample Event',
            'date': '2024-09-01',
            'description': 'This is a sample event.'
        })
        self.assertEqual(response.status_code, 302)  # assuming a redirect on success
        self.assertRedirects(response, reverse('events'))