from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from sound_frequencies.core.mixins import BootstrapFormMixin
from sound_frequencies.profiles.models import Profile

UserModel = get_user_model()


class SignUpForm(BootstrapFormMixin, UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', ]


class LogInForm(BootstrapFormMixin, AuthenticationForm):
    pass


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'is_complete']
