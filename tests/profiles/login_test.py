from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.testing_utils.base_test_data import SoundFrequenciesTestCase
UserModel = get_user_model()


class LogInTests(SoundFrequenciesTestCase):
    def test_postLogIn_whenUsernamePasswordValid__shouldLoginIn(self):
        user = UserModel.objects.create_user(
            username='Test_username',
            password='Test_Password!@123'
        )
        response = self.client.post(reverse('log in'), data={
            'username': 'Test_username',
            'password': 'Test_Password!@123',
        })

        self.assertEqual(302, response.status_code)
        logged_in_user = UserModel.objects.filter(pk=user.id).first()

        self.assertEqual(user.username, logged_in_user.username)
