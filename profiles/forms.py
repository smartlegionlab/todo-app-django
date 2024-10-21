from django import forms

from profiles.models import Profile
from django.contrib.auth.forms import PasswordChangeForm


class ProfileSettingsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'first_name', 'last_name', 'telegram_id']
        labels = {
            'email': 'E-mail',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'telegram_id': 'Telegram ID',
        }


class ProfilePasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Confirm new password', widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ('old_password', 'new_password1', 'new_password2')
