from django.urls import reverse

from sound_frequencies.web.models import Event
from tests.testing_utils.base_test_data import SoundFrequenciesTestCase


class EventDeleteTest(SoundFrequenciesTestCase):
    def test_postDeleteEvent_whenLoggedInUserDeleteEvent__shouldDelete(self):
        event = Event.objects.create(
            name='Test event',
            city='test city',
            location='test location',
            image='path/to/image.jpg',
            description='test description',
            date='2021-08-09',
            time='16:00:00',
            tickets_link='https://tickets.bg',
            user=self.user
        )

        self.client.force_login(self.user)
        response = self.client.post(reverse('event delete', kwargs={'pk': event.pk}))

        self.assertEqual(302, response.status_code)

        user_events = Event.objects.filter(user_id=self.user.id)

        self.assertListEqual([], list(user_events))
