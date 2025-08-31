from django import forms
from .models import Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MoreDetails

class Tweetform(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text','photo']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email Address.')

    class Meta:
        model = User
        fields = ('username', 'email','password1','password2')

class BlogForm(forms.ModelForm):
    class Meta:
        model = MoreDetails
        fields = ['title','author']
        widgets = {
            'content': forms.Textarea(attrs={'rows':15, 'cols':80}),
        }