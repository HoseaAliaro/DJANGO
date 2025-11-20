from django import forms
from . models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['firstName', 'secondName', 'email','regNo','age' ]

# user authentication
class CustomUser(UserCreationForm):
    class Meta:
        model= User
        fields=['username','password1','password2']
