from django.conf import settings
from securitas.auth.methods import twoauth_methods


def get_login_template():
    """
    Returns the login template path
    """
    template = 'admin/securitas_login'
    if 'grappelli' in settings.INSTALLED_APPS:
        template += '_grappelli'

    return "%s.html" % template


def get_twofactor_method(search_name):
    """
    Returns a twofactor method for a given name
    """
    for name, method in twoauth_methods:
        if name == search_name:
            return method
    return False
