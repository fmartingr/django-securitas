#from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from securitas.utils import get_login_template
from securitas.auth.forms import SecuritasAuthenticationForm
from securitas import settings as securitas_settings


class SecuritasAdminSite(AdminSite):
    """
    Custom securitas admin site
    """

    def __init__(self, *args, **kwargs):
        if not securitas_settings.OTP_OR_PASSWORD:
            self.login_template = get_login_template()
            self.login_form = SecuritasAuthenticationForm
        super(SecuritasAdminSite, self).__init__(*args, **kwargs)

site = SecuritasAdminSite()
