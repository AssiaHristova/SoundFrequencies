from django.urls import reverse

from sound_frequencies.web.models import Event
from tests.testing_utils.base_test_data import SoundFrequenciesTestCase


class EventListTests(SoundFrequenciesTestCase):
    def getEventsList__ifUserHasEvents__shouldGetUserEventsAndOtherEvents(self):
        past_event = Event.objects.create(
            name='past event',
            city='Test city',
            location='Test location',
            image='path/to/image.png',
            description='test description',
            date='2020-05-04',
            time='16:00:00',
            tickets_link='https://articles.bg',
            user=self.user
        )

        upcoming_event = Event.objects.create(
            name='upcoming event',
            city='Test city',
            location='Test location',
            image='path/to/image.png',
            description='test description',
            date='2021-11-12',
            time='16:00:00',
            tickets_link='https://articles.bg',
            user=self.user
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('events list'))

        past_events = list(response.context['past_events'])
        upcoming_events = list(response.context['upcoming_events'])
        user_events = list(response.context['user_events'])

        self.assertEqual(200, response.status_code)
        self.assertListEqual([past_event], past_events)
        self.assertListEqual([upcoming_event], upcoming_events)
        self.assertListEqual([past_event, upcoming_event], user_events)


