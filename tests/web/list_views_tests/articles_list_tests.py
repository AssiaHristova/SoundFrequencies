from django.urls import reverse

from sound_frequencies.web.models import Article
from tests.testing_utils.base_test_data import SoundFrequenciesTestCase


class ArticlesListTests(SoundFrequenciesTestCase):
    def test_getArticlesList__ifUserHasArticles__shouldGetUserArticlesAndOtherArticles(self):
        article = Article.objects.create(
            title='Test Article',
            image_url='https://images.bg',
            text='test article text',
            date='2021-08-09',
            source='https://articles.bg',
            author='test author',
            user=self.user
        )

        article_2 = Article.objects.create(
            title='Test Article',
            image_url='https://images.bg',
            text='test article text',
            date='2021-08-09',
            source='https://articles.bg',
            author='test author',
            user=self.user_2
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('articles list'))

        user_articles = list(response.context['user_articles'])
        articles = list(response.context['articles'])

        self.assertListEqual([article], user_articles)
        self.assertListEqual([article, article_2], articles)




