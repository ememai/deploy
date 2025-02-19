# Generated by Django 5.1.4 on 2025-02-19 19:46

import cloudinary.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_myfiles_files_alter_myfiles_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='LcMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images')),
                ('files', models.FileField(upload_to='documents')),
            ],
        ),
        migrations.AddField(
            model_name='myfiles',
            name='files',
            field=cloudinary.models.CloudinaryField(default=django.utils.timezone.now, max_length=255, verbose_name='files'),
            preserve_default=False,
        ),
    ]
