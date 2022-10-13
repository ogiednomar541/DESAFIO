from django.contrib import admin

from apps.modelo.models import Marca, Modelo


admin.site.register(Marca)
admin.site.register(Modelo)