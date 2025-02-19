# Generated by Django 5.1.4 on 2025-02-19 20:47

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_lcmedia_myfiles_files'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LcMedia',
        ),
        migrations.AlterField(
            model_name='myfiles',
            name='files',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='files'),
        ),
        migrations.AlterField(
            model_name='myfiles',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
    ]
