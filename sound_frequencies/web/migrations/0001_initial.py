# Generated by Django 3.2.6 on 2021-08-04 22:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sound_frequencies.web.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='artists')),
                ('bio', models.TextField()),
                ('links', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(default='Sofia', max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='events')),
                ('description', models.TextField()),
                ('tickets_link', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Merchandise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='merchandise')),
                ('color', models.CharField(choices=[('BLACK', 'black'), ('WHITE', 'white')], max_length=15)),
                ('size', models.CharField(blank=True, choices=[('SMALL', 'S'), ('MEDIUM', 'M'), ('LARGE', 'L'), ('EXTRA_LARGE', 'XL'), ('EXTRA_EXTRA_LARGE', 'XXL')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, upload_to='videos')),
                ('file_url', models.URLField(blank=True)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('artist', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='web.artist')),
                ('event', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='web.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='releases/files')),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='releases/images')),
                ('description', models.TextField()),
                ('label', models.CharField(max_length=30)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.artist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('file', models.ImageField(upload_to=sound_frequencies.web.models.generate_folder)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, upload_to='mixes/files')),
                ('file_url', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='mixes/images')),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.artist')),
                ('event', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='web.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_url', models.URLField()),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('source', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
