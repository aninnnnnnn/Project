from django.contrib.auth.forms import UserCreationForm
from .models import User, Album
from django.forms import ModelForm


class MyUserCreationFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

