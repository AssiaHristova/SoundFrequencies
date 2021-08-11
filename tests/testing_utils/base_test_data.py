
from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from sound_frequencies.web.models import Event

UserModel = get_user_model()


class SoundFrequenciesTestCase(TestCase):
    UserModel = get_user_model()
    logged_in_user_username = 'raya'
    logged_in_user_password = 'Muncheto2017'
    logged_in_user_2_username = 'raya2'
    logged_in_user_2_password = 'Muncheto2017'

    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(username=self.logged_in_user_username, password=self.logged_in_user_password)
        self.user_2 = UserModel.objects.create_user(username=self.logged_in_user_2_username, password=self.logged_in_user_2_password)



    def assertListEmpty(self, ll):
        return self.assertListEqual([], ll)





