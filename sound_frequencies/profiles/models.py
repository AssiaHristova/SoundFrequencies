from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
        ]
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    profile_image = models.ImageField(upload_to='profiles', blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE,  primary_key=True,)
    is_complete = models.BooleanField(default=False)


from sound_frequencies.core.signals import *
