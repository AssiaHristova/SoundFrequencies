from django.urls import reverse

from sound_frequencies.web.models import Release, Artist
from tests.testing_utils.base_test_data import SoundFrequenciesTestCase


class ReleaseListTest(SoundFrequenciesTestCase):
    def test_getReleaseList__ifObjectsExists__shouldGetObjects(self):
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
        release_2 = Release.objects.create(
            title='Test release',
            image='path/to/image.jpg',
            description='test desc',
            date='2021-08-09',
            price=10,
            artist=artist,
            link_to_purchase='https://articles.bg'
        )

        response = self.client.get(reverse('releases list'))

        releases = list(response.context['release_list'])

        self.assertListEqual([release, release_2], releases)
