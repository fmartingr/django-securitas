from django.db import models
from django.conf import settings
from securitas.auth.methods import twoauth_methods


class TwoFactor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    type = models.CharField(
        max_length=16,
        choices=twoauth_methods
    )
    secret_id = models.IntegerField()
    secret_key = models.CharField(max_length=128)

    class Meta:
        app_label = 'securitas'


from django.contrib import admin
admin.site.register(TwoFactor)
