from django.contrib import admin
from django.utils.text import slugify

from diarios.models import Entrada, Topico

# Register your models here.

admin.site.register(Topico)
admin.site.register(Entrada)
