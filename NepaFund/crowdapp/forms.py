from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.forms import fields, widgets
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation

class ChangePassword(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old password"),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'autofocus':True, 'class':'form-control'}))
    new_password1 = forms.CharField(label=_("New Password"),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'autofocus':True, 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New password"),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'autofocus':True, 'class':'form-control'}))


class MyPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(label=_('Email'),max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1=forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(label='Confirm New Password',widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
