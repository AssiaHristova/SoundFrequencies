from django.urls import reverse

from sound_frequencies.web.models import Photo, Event
from tests.testing_utils.base_test_data import SoundFrequenciesTestCase


class PhotosDetailsTest(SoundFrequenciesTestCase):
    def test_getPhotos_whenLoggedInUser__shouldGetAllPhotos(self):
        event = Event.objects.create(
            name='Test event',
            city='Test city',
            location='Test location',
            image='path/to/image.png',
            description='test description',
            date='2021-08-09',
            time='16:00:00',
            tickets_link='https://articles.bg',
            user=self.user
        )

        photo = Photo.objects.create(
            name='Test photo',
            image='path/to/image.jpg',
            event=event,
            user=self.user
        )

        event_2 = Event.objects.create(
            name='Test event',
            city='Test city',
            location='Test location',
            image='path/to/image.png',
            description='test description',
            date='2021-08-09',
            time='16:00:00',
            tickets_link='https://articles.bg',
            user=self.user
        )

        photo_2 = Photo.objects.create(
            name='Test photo',
            image='path/to/image.jpg',
            event=event,
            user=self.user_2
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('photos list'))

        user_photos = list(response.context['user_photos'])
        events_with_photos = list(response.context['events_with_photos'])
        photos_ordered_by_event = list(response.context['photos_ordered_by_event'])

        self.assertListEqual([photo], user_photos)
        self.assertListEqual([event], events_with_photos)
        self.assertListEqual([photo, photo_2], photos_ordered_by_event)


