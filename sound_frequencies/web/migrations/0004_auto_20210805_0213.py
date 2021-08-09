# Generated by Django 3.2.6 on 2021-08-04 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_video_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.artist'),
        ),
        migrations.AlterField(
            model_name='video',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.event'),
        ),
    ]
