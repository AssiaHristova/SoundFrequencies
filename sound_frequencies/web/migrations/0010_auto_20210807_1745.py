# Generated by Django 3.2.6 on 2021-08-07 14:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20210807_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='release',
            name='file',
        ),
        migrations.RemoveField(
            model_name='release',
            name='user',
        ),
        migrations.AddField(
            model_name='merchandise',
            name='link_to_purchase',
            field=models.URLField(default='https://www.emag.bg/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='release',
            name='link_to_purchase',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
