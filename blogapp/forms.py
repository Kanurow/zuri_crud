from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CommentForm(forms.ModelForm):
    class Meta:
        fields = ('authors_name', 'comment_body')
        widgets = {
            'authors_name': forms.TextInput(attrs={'class': 'form-control'}),
            'comment_body': forms.Textarea(attrs={'class': 'form-control'}),
        }