from enum import unique
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.validators import RegexValidator

from user.models import User
from user.validators import *

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'name',
            'bio', 
            'sphere',
            'image'
        )
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control custom-file-upload'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(latin_validator)
        self.fields['password2'].validators.append(password_validator)

class ProfileUpdateForm(forms.ModelForm):
    def clean_username(self):
        # Получаем новое значение username из формы
        new_username = self.cleaned_data.get('username')
        
        # Получаем текущего пользователя
        user = self.instance
        
        # Вызываем валидатор для проверки ограничения на изменение имени пользователя
        username_change_limit_validator(user, new_username)
        
        return new_username
    
    class Meta:
        model = User
        fields = ['username', 'name', 'bio', 'sphere', 'image']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Bio'}),
            'sphere': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sphere'}),
            'image': forms.FileInput(attrs={'class': 'form-control custom-file-upload'}),
        }

