from django.urls import reverse

from sound_frequencies.web.models import Photo, Event
from tests.testing_utils.base_test_data import SoundFrequenciesTestCase


class PhotoDeleteTest(SoundFrequenciesTestCase):
    def test_postDeletePhoto_whenLoggedInUserDeleteEvent__shouldDelete(self):
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
        photo = Photo.objects.create(
            name='Test photo',
            image='path/to/image/.jpg',
            event=event,
            user=self.user
        )

        self.client.force_login(self.user)
        response = self.client.post(reverse('photo delete', kwargs={'pk': photo.pk}))

        self.assertEqual(302, response.status_code)

        user_photos = Photo.objects.filter(user_id=self.user.id)

        self.assertListEqual([], list(user_photos))
