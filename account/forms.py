from django import forms
from django.contrib.auth.models import User
from .models import Profile
import re

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean(self):
        cd = self.cleaned_data
        len_initial = len(cd['password'])
        sub_str = re.sub('[^가-힝0-9a-zA-z]', '', cd['password'])
        len_new = len(sub_str)

        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if len_initial != len_new and password1 == password2:
            return cd
        elif len_initial == len_new:
            raise forms.ValidationError('Please 특수문자')
        else:
            raise forms.ValidationError('Passwords don\'t match.')

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('Passwords don\'t match.')
    #     return cd

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')