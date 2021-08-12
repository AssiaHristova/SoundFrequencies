from django.urls import reverse

from sound_frequencies.web.models import Merchandise
from tests.testing_utils.base_test_data import SoundFrequenciesTestCase


class MerchandiseListTest(SoundFrequenciesTestCase):
    def test_getMerchandiseList__ifObjectsExists__shouldGetObjects(self):
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

        merch_2 = Merchandise.objects.create(
            title='Test merch 2',
            image='path/to/images.png',
            description='test desc',
            date='2021-08-09',
            price=10,
            color='test artist',
            size='test artist',
            link_to_purchase='https://articles.bg'
        )

        response = self.client.get(reverse('merches list'))

        merches = list(response.context['merchandise_list'])

        self.assertListEqual([merch_1, merch_2], merches)
