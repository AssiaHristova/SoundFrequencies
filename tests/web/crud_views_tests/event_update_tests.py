from django.urls import reverse

from sound_frequencies.web.models import Event
from tests.testing_utils.base_test_data import SoundFrequenciesTestCase


class EventUpdateTest(SoundFrequenciesTestCase):
    def test_postUpdateEvent_whenLoggedInUserUpdateEvent__shouldUpate(self):
        name = 'Test event'
        name_2 = 'Test event_2'
        image = 'path/to/image.jpg'
        city = 'test city'
        date = '2021-08-09'
        time = '16:00:00'
        tickets_link = 'https://tickets.bg'
        location = 'test location'
        description = 'test description'

        event = Event.objects.create(
            name=name,
            city=city,
            location=location,
            image=image,
            description=description,
            date=date,
            time=time,
            tickets_link=tickets_link,
            user=self.user
        )

        self.client.force_login(self.user)

        response = self.client.post(reverse('event update', kwargs={'pk': event.pk}), data={
            'name': name_2,
            'city': city,
            'location': location,
            'date': date,
            'time': time,
            'image': image,
            'description': description,
            'tickets_link': tickets_link,
            'user': self.user
        })

        self.assertEqual(302, response.status_code)

        user_events = Event.objects.filter(user_id=self.user.id)
        updated_event = user_events.first()

        self.assertEqual(name_2, updated_event.name)
