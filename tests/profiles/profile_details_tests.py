import random
from os.path import join

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from sound_frequencies.profiles.models import Profile
from tests.profiles.profile_uploads_tests import SoundFrequenciesTestCase


class ProfileDetailsTest(SoundFrequenciesTestCase):
    def test_getDetails_whenLoggedInUser__shouldGetDetails(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile details'))

        profile = response.context['profile']

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.user.id, profile.user_id)

    def test_postDetails_whenLoggedInUserUpdateDetails__shouldUpdateDetails(self):
        path_to_image = join(settings.BASE_DIR, 'tests', 'testing_utils', 'test_image.jpg')
        file_name = f'{random.randint(1, 1000)}-test_image.jpg'
        image = SimpleUploadedFile(
            name=file_name,
            content=open(path_to_image, 'rb').read(),
            content_type='image/jpeg'
        )
        first_name = 'test first name'
        last_name = 'test last name'
        age = 20
        gender = 'M'

        self.client.force_login(self.user)

        response = self.client.post(reverse('profile details'), data={
            'profile_image': image,
            'first_name': first_name,
            'last_name': last_name,
            'age': age,
            'gender': gender,
        })
        self.assertEqual(302, response.status_code)

        profile = Profile.objects.get(pk=self.user.id)

        self.assertTrue(str(profile.profile_image).endswith(file_name))
        self.assertEqual(first_name, profile.first_name)
        self.assertEqual(last_name, profile.last_name)
        self.assertEqual(age, profile.age)
        self.assertEqual(gender, profile.gender)




