# Generated by Django 4.2.3 on 2023-08-07 16:42

from django.db import migrations, models
import video.models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0008_rename_tancos_post_adatkozlo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(upload_to=video.models.upload_location),
        ),
    ]