from django.urls import reverse

from sound_frequencies.web.models import Article
from tests.testing_utils.base_test_data import SoundFrequenciesTestCase


class ArticleCreateTest(SoundFrequenciesTestCase):
    def test_postCreateArticle_whenLoggedInUserCreateArticle__shouldCreate(self):
        title = 'Test Article'
        image_url = 'https://images.bg'
        text = 'test article text'
        date = '2021-08-09'
        source = 'https://articles.bg'
        author = 'test author'

        self.client.force_login(self.user)
        response = self.client.post(reverse('article create'), data={
            'title': title,
            'image_url': image_url,
            'text': text,
            'date': date,
            'source': source,
            'author': author,
            'user': self.user
        })

        self.assertEqual(302, response.status_code)

        user_articles = Article.objects.filter(user_id=self.user.id)
        article = user_articles.first()

        self.assertEqual(title, article.title)
        self.assertEqual(image_url, article.image_url)
        self.assertEqual(text, article.text)
        self.assertEqual(date, str(article.date))
        self.assertEqual(source, article.source)
        self.assertEqual(author, article.author)
        self.assertEqual(self.user, article.user)
