from django.urls import reverse

from sound_frequencies.web.models import Event, Release, Merchandise, Artist
from tests.testing_utils.base_test_data import SoundFrequenciesTestCase


class HomePageTest(SoundFrequenciesTestCase):
    def test_getHomePage__ifObjectsExists__shouldGetObjects(self):
        artist = Artist.objects.create(
            name='Test artist',
            image='path/to/image.jpg',
            bio='test bio',
            links='https://articles.bg'
        )

        release = Release.objects.create(
            title='Test release',
            image='path/to/image.jpg',
            description='test desc',
            date='2021-08-09',
            price=10,
            artist=artist,
            link_to_purchase='https://articles.bg'
        )

        event = Event.objects.create(
            name='Test event',
            city='Test city',
            location='Test location',
            image='path/to/image.png',
            description='test description',
            date='2021-09-09',
            time='16:00:00',
            tickets_link='https://articles.bg',
            user=self.user
        )

        merch_1 = Merchandise.objects.create(
            title='Test merch',
            image='path/to/images.png',
            description='test desc',
            date='2021-08-09',
            price=10,
            color='test artist',
            size='test artist',
            link_to_purchase='https://articles.bg'
        )

        response = self.client.get(reverse('home page'))

        releases_to_show = list(response.context['releases'])
        event_to_show = response.context['event']
        merches = list(response.context['merch_list'])

        self.assertEqual(event, event_to_show)
        self.assertListEqual([release], releases_to_show)
        self.assertListEqual([merch_1], merches)

    def test_getHomePage__ifNoObjects__shouldGetEmpty(self):
        response = self.client.get(reverse('home page'))

        releases_to_show = list(response.context['releases'])
        event_to_show = response.context['event']
        merches = list(response.context['merch_list'])

        self.assertEqual(None, event_to_show)
        self.assertListEqual([], releases_to_show)
        self.assertListEqual([], merches)


