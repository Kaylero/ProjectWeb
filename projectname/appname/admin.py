from django.contrib import admin

# Register your models here.

from appname.models import Sobre, Empresa
admin.site.register(Sobre)
admin.site.register(Empresa)
