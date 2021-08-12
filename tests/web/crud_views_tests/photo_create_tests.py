import random
from os.path import join

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from sound_frequencies.web.models import Photo, Event
from tests.testing_utils.base_test_data import SoundFrequenciesTestCase


class PhotoCreateTest(SoundFrequenciesTestCase):
    def test_postCreatePhoto_whenLoggedInUserCreatePhoto__shouldCreate(self):
        path_to_image = join(settings.BASE_DIR, 'tests', 'testing_utils', 'test_image.jpg')
        file_name = f'{random.randint(1, 1000)}-test_image.jpg'
        path_to_image_2 = join(settings.BASE_DIR, 'tests', 'testing_utils', 'test_image_2.jpg')
        file_name_2 = f'{random.randint(1, 1000)}-test_image_2.jpg'
        image = SimpleUploadedFile(
            name=file_name,
            content=open(path_to_image, 'rb').read(),
            content_type='image/jpeg'
        )
        image_2 = SimpleUploadedFile(
            name=file_name_2,
            content=open(path_to_image, 'rb').read(),
            content_type='image/jpeg'
        )
        event = Event.objects.create(
            name='past event',
            city='Test city',
            location='Test location',
            image=image_2,
            description='test description',
            date='2020-05-04',
            time='16:00:00',
            tickets_link='https://articles.bg',
            user=self.user
        )

        name = 'Test photo'

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
        self.assertTrue(str(photo.image).endswith(file_name))
        self.assertEqual(event, photo.event)
        self.assertEqual(self.user, photo.user)
