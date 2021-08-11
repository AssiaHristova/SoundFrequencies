
from os.path import join

from django.conf import settings
from django.urls import reverse

from sound_frequencies.web.models import Photo, Event
from tests.testing_utils.base_test_data import SoundFrequenciesTestCase


class PhotoCreateTest(SoundFrequenciesTestCase):
    def test_postCreatePhoto_whenLoggedInUserCreatePhoto__shouldCreate(self):
        event = Event.objects.create(
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
        path_to_image = join(settings.BASE_DIR, 'tests', 'testing_utils', 'test_image.jpg')
        name = 'Test photo'
        image = open(path_to_image, 'rb').read()

        self.client.force_login(self.user)
        response = self.client.post(reverse('photo create'), data={
            'name': name,
            'image': image,
            'event': event,
            'user': self.user
        })

        self.assertEqual(302, response.status_code)

        user_photos = Photo.objects.filter(user_id=self.user.id)
        photo = user_photos.first()

        self.assertEqual(name, photo.name)
        self.assertEqual(image, photo.image)
        self.assertEqual(event, photo.event)
        self.assertEqual(self.user, photo.user)
