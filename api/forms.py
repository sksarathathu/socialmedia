from django import forms
from api.models import Posts,Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["title","image","description"]

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=["comment"]


class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


    class Meta:
        model=User
        fields=["email","username","password1","password2"]
        widgets={
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"})
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))