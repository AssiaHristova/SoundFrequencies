import sys

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils import timezone
from djmoney.models.fields import MoneyField
from io import BytesIO
from django.db import models
from PIL import Image


UserModel = get_user_model()


class Article(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField()
    text = models.TextField()
    date = models.DateField()
    source = models.URLField()
    author = models.CharField(max_length=50)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Event(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=20, default='Sofia')
    location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    image = models.ImageField(upload_to='events')
    description = models.TextField()
    tickets_link = models.URLField(blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='artists')
    bio = models.TextField()
    links = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class Release(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='releases/images')
    description = models.TextField()
    price = MoneyField(max_digits=9, decimal_places=2, default_currency='BGN', default=10)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    label = models.CharField(max_length=30)
    link_to_purchase = models.URLField()

    def __str__(self):
        return self.title


def generate_folder(self, filename):
    folder = "photos/%s/%s" % (self.event.name, filename)
    return folder


def generate_image_name(image):
    image_name = "%s.jpg.zip" % image.name.split('.')[0]
    return image_name


def compress_image(image):
    temporary_image = Image.open(image)
    thumb_io = BytesIO()
    temporary_image.resize((1020, 573))
    temporary_image.save(thumb_io, format='JPEG', quality=80)
    thumb_io.seek(0)
    compressed_image = InMemoryUploadedFile(thumb_io, 'ImageField', generate_image_name, 'image/jpeg', sys.getsizeof(thumb_io), None)
    return compressed_image


class Photo(models.Model):
    name = models.CharField(max_length=50, default='myphoto.jpg')
    image = models.ImageField(upload_to=generate_folder)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=3)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Merchandise(models.Model):
    COLOR_CHOICES = [
        ('BLACK', 'black'),
        ('WHITE', 'white')
    ]
    SIZE_CHOICES = [
        ('SMALL', 'S'),
        ('MEDIUM', 'M'),
        ('LARGE', 'L'),
        ('EXTRA_LARGE', 'XL'),
        ('EXTRA_EXTRA_LARGE', 'XXL')
    ]
    title = models.CharField(max_length=100)
    price = MoneyField(max_digits=9, decimal_places=2, default_currency='BGN', default=10)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='merchandise')
    color = models.CharField(max_length=15, choices=COLOR_CHOICES)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES, blank=True)
    link_to_purchase = models.URLField()

    def __str__(self):
        return self.title


