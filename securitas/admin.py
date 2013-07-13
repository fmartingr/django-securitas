#from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django import forms
from securitas.utils import get_login_template


class SecuritasAuthenticationForm(AuthenticationForm):
    "Custom authentication form with the OTP field."
    otp = forms.CharField(required=False, widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        # TODO fix STR on python-yubikey package
        otp = str(self.cleaned_data.get('otp'))

        if username and password:
            self.user_cache = authenticate(username=username,
                                           password=password,
                                           otp=otp)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            elif not self.user_cache.is_active:
                raise forms.ValidationError(
                    self.error_messages['inactive'],
                    code='inactive',
                )
        return self.cleaned_data


class SecuritasAdminSite(AdminSite):
    "..."
    login_template = get_login_template()
    login_form = SecuritasAuthenticationForm

site = SecuritasAdminSite()
