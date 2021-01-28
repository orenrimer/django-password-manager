from django import forms
from .models import Entry

class EntryCreateForm(forms.ModelForm):
    password = forms.CharField(max_length=200, label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Entry
        fields = ('email', 'username', 'password', 'site_name', 'site_url', 'notes')

    def clean_site_name(self):
        site_name = self.cleaned_data.get('site_name')
        site_name = site_name.lower().strip()
        return site_name

    def clean_site_url(self):
        site_url = self.cleaned_data.get('site_url')
        site_url = site_url.lower().strip()
        return site_url


class EntryUpdateForm(forms.ModelForm):
    password = forms.CharField(max_length=200, label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Entry
        fields = ('email', 'username', 'password', 'site_name', 'site_url', 'notes')

    def clean_site_name(self):
        site_name = self.cleaned_data.get('site_name')
        site_name = site_name.lower().replace(' ', '')
        return site_name

    def clean_site_url(self):
        site_url = self.cleaned_data.get('site_url')
        site_url = site_url.lower().replace(' ', '')
        return site_url