from django import forms
from django.forms import FileField

from sound_frequencies.web.models import Event, Article, Photo


#class PhotoUploadForm(forms.Form):
 #   photos = FileField(allow_empty_file=True, widget=forms.ClearableFileInput(attrs={'multiple': True}))


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['user',]


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['user', ]


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['user', 'name']





