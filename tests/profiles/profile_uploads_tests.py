from django.urls import reverse

from sound_frequencies.web.models import Article, Event, Photo
from tests.testing_utils.base_test_data import SoundFrequenciesTestCase


class ProfileUploadsTest(SoundFrequenciesTestCase):
    def test_getUploads_whenLoggedInUser__WhenNoUploads__shouldGetEmpty(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile uploads'))

        articles = response.context['articles']
        events = response.context['events']
        photos = response.context['photos']

        self.assertEqual(200, response.status_code)
        self.assertListEmpty(list(articles))
        self.assertListEmpty(list(events))
        self.assertListEmpty(list(photos))

    def test_getUploads_whenLoggedInUser__WhenUploads__shouldGetUploads(self):
        article = Article.objects.create(
            title='Test Article',
            image_url='https://images.bg',
            text='test article text',
            date='2021-08-09',
            source='https://articles.bg',
            author='test author',
            user=self.user
        )

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
            name ='test name',
            image='path/to/image.png',
            event=event,
            user=self.user
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('profile uploads'))

        articles = list(response.context['articles'])
        events = list(response.context['events'])
        photos = list(response.context['photos'])

        self.assertListEqual([article], articles)
        self.assertListEqual([event], events)
        self.assertListEqual([photo], photos)
