from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate
from django import forms
#from django.conf import settings


class SecuritasAuthenticationForm(AuthenticationForm):
    """
    Securitas authentication form defined by the settings.
    Adds the OTP field if it is needed.
    """
    otp = forms.CharField(required=False, widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': _("Your login credentials were invalid."),
        'inactive': _("This account is inactive."),
    }

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
                    self.error_messages['invalid_login'])
            elif not self.user_cache.is_active:
                raise forms.ValidationError(
                    self.error_messages['inactive'])

        return self.cleaned_data
