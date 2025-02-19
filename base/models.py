from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=1000)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000)
    members = models.ManyToManyField(User, related_name = 'members')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content[:2]
    

class MyFiles(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image', folder='images', blank=True)  # Files saved to MEDIA_ROOT/images/
    files = CloudinaryField('files', resource_type='raw', folder='documents', blank=True)
    
# class LcMedia(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='images')  # Files saved to MEDIA_ROOT/images/
#     files = models.FileField(upload_to='documents')
    