from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'topic', 'description']

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'is_superuser']

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['content']
    