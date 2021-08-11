from django import forms
from django.forms import FileField

from sound_frequencies.core.mixins import BootstrapFormMixin
from sound_frequencies.web.models import Event, Article, Photo


class EventForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['user',]


class ArticleForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['user', ]


class PhotoForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['user', ]





