#from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django import forms
from securitas.utils import get_login_template
from securitas.auth.forms import SecuritasAuthenticationForm


class SecuritasAdminSite(AdminSite):
    "..."
    login_template = get_login_template()
    login_form = SecuritasAuthenticationForm

site = SecuritasAdminSite()
