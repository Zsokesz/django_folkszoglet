# Generated by Django 4.2.3 on 2023-07-24 17:46

from django.db import migrations, models
import video.models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_post_video_from_url_alter_post_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, default='', upload_to=video.models.upload_location),
        ),
        migrations.AlterField(
            model_name='post',
            name='video_from_url',
            field=models.TextField(blank=True, default='', max_length=100),
        ),
    ]
