import random
from os.path import join

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from sound_frequencies.web.models import Event
from tests.testing_utils.base_test_data import SoundFrequenciesTestCase


class EventCreateTest(SoundFrequenciesTestCase):
    def test_postCreateEvent_whenLoggedInUserCreateEvent__shouldCreate(self):
        path_to_image = join(settings.BASE_DIR, 'tests', 'testing_utils', 'test_image.jpg')
        file_name = f'{random.randint(1, 1000)}-test_image.jpg'
        image = SimpleUploadedFile(
            name=file_name,
            content=open(path_to_image, 'rb').read(),
            content_type='image/jpeg'
        )
        name = 'Test event'
        city = 'test city'
        date = '2021-08-09'
        time = '16:00:00'
        tickets_link = 'https://tickets.bg'
        location = 'test location'
        description = 'test description'

        self.client.force_login(self.user)
        response = self.client.post(reverse('event create'), data={
            'name': name,
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
        event = user_events.first()

        self.assertEqual(name, event.name)
        self.assertTrue(str(event.image).endswith(file_name))
        self.assertEqual(city, event.city)
        self.assertEqual(date, str(event.date))
        self.assertEqual(time, str(event.time))
        self.assertEqual(tickets_link, event.tickets_link)
        self.assertEqual(location, event.location)
        self.assertEqual(description, event.description)
        self.assertEqual(self.user, event.user)
