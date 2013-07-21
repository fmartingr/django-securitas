django-securitas
================

Moar security for your django apps


# Installation

Install django-securitas
```
pip install django-securitas
```

Configure the new admin site:
```
from django.contrib import admin
from securitas.admin import site as securitas_adminsite

admin.site = securitas_adminsite
```

Remember to syncdb and migrate!
