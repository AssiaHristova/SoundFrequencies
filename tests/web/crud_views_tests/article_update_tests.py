from django.urls import reverse

from sound_frequencies.web.models import Article
from tests.testing_utils.base_test_data import SoundFrequenciesTestCase


class ArticleUpdateTest(SoundFrequenciesTestCase):
    def test_postUpdateArticle_whenLoggedInUserUpdateArticle__shouldUpate(self):
        title = 'Test Article'
        title_2 = 'Test Article_2'
        image_url = 'https://images.bg'
        text = 'test article text'
        date = '2021-08-09'
        source = 'https://articles.bg'
        author = 'test author'

        article = Article.objects.create(
            title=title,
            image_url=image_url,
            text=text,
            date=date,
            source=source,
            author=author,
            user=self.user
        )

        self.client.force_login(self.user)

        response = self.client.post(reverse('article update', kwargs={'pk': article.pk}), data={
            'title': title_2,
            'image_url': image_url,
            'text': text,
            'date': date,
            'source': source,
            'author': author,
            'user': self.user,
        })


        self.assertEqual(302, response.status_code)

        user_articles = Article.objects.filter(user_id=self.user.id)
        updated_article = user_articles.first()
        
        self.assertEqual(title_2, updated_article.title)
