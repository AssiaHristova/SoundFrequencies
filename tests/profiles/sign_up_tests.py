from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.testing_utils.base_test_data import SoundFrequenciesTestCase
UserModel = get_user_model()


class SignUpTests(SoundFrequenciesTestCase):
    def test_postSignUp_whenUsernamePasswordValid__shouldSignUpAndLoginIn(self):
        response = self.client.post(reverse('sign up'), data={
            'username': 'Test_username',
            'password1': 'Test_Password!@123',
            'password2': 'Test_Password!@123'
        })

        self.assertEqual(302, response.status_code)
        user = UserModel.objects.all().last()

        self.assertEqual('Test_username', user.username)


