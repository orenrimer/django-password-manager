from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Account


class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login credentials.")


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(max_length=20, label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'username')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = Account.objects.exclude(pk=self.instance.pk).filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email name is already taken.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = Account.objects.exclude(pk=self.instance.pk).filter(username=username)
        if qs.exists():
            raise forms.ValidationError("User name is already taken.")
        return username