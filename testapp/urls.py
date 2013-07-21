from django.conf.urls import patterns, include, url

from django.contrib import admin

# Adding this two lines to enables the securitas admin site
from securitas.admin import site
admin.site = site

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
)
