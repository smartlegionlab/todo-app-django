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


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = Profile
        fields = ['email', 'first_name', 'last_name', 'telegram_id', 'password', 'password_confirm']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
