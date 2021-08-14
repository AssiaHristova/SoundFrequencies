from django.urls import reverse

from sound_frequencies.web.models import Article
from tests.testing_utils.base_test_data import SoundFrequenciesTestCase


class ArticleDeleteTest(SoundFrequenciesTestCase):
    def test_postDeleteArticle_whenLoggedInUserDeleteArticle__shouldDelete(self):
        article = Article.objects.create(
            title='Test Article',
            image_url='https://images.bg',
            text='test article text',
            date='2021-08-09',
            source='https://articles.bg',
            author='test author',
            user=self.user
        )

        self.client.force_login(self.user)
        response = self.client.post(reverse('article delete', kwargs={'pk': article.pk}))

        self.assertEqual(302, response.status_code)

        user_articles = Article.objects.filter(user_id=self.user.id)

        self.assertListEqual([], list(user_articles))
