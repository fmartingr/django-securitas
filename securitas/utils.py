from django.conf import settings
from securitas.auth.methods import twoauth_methods


def get_login_template():
    template = 'admin/securitas_login'
    if 'grappelli' in settings.INSTALLED_APPS:
        template += '_grappelli'

    return "%s.html" % template


def get_twofactor_method(method):
    for k, v in twoauth_methods:
        if k == method:
            return v
    return False
