from django.urls import reverse

from sound_frequencies.web.models import Event, Photo
from tests.testing_utils.base_test_data import SoundFrequenciesTestCase


class PhotoUpdateTest(SoundFrequenciesTestCase):
    def test_postUpdatePhoto_whenLoggedInUserUpdatePhoto__shouldUpate(self):
        name = 'Test photo'
        name_2 = 'Test photo_2'
        image = 'path/to/image/.jpg'

        event = Event.objects.create(
            name='test event',
            city='Test city',
            location='Test location',
            image='path/to/image.png',
            description='test description',
            date='2020-05-04',
            time='16:00:00',
            tickets_link='https://articles.bg',
            user=self.user
        )
        photo = Photo.objects.create(
            name=name,
            image=image,
            event=event,
            user=self.user
        )

        self.client.force_login(self.user)

        response = self.client.post(reverse('photo update', kwargs={'pk': photo.pk}), data={
            'name': name_2,
            'image': image,
            'event': event,
            'user': self.user
        })

        self.assertEqual(302, response.status_code)

        user_photos = Photo.objects.filter(user_id=self.user.id)
        updated_photo = user_photos.first()

        self.assertEqual(name_2, updated_photo.name)
