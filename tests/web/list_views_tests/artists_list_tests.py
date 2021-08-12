from django.urls import reverse

from sound_frequencies.web.models import Artist
from tests.testing_utils.base_test_data import SoundFrequenciesTestCase


class ArtistsListTest(SoundFrequenciesTestCase):
    def test_getArtistsList__ifObjectsExists__shouldGetObjects(self):
        artist = Artist.objects.create(
            name='Test artist',
            image='path/to/image.jpg',
            bio='test bio',
            links='https://articles.bg'
        )

        artist_2 = Artist.objects.create(
            name='Test artist 2',
            image='path/to/image.jpg',
            bio='test bio',
            links='https://articles.bg'
        )

        response = self.client.get(reverse('artists list'))

        artists = list(response.context['artist_list'])

        self.assertListEqual([artist, artist_2], artists)
