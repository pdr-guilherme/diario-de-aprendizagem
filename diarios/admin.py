from django.contrib import admin
from django.utils.text import slugify

from diarios.models import Entrada, Topico


# Register your models here.
class TopicoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["topico"]}


# class EntradaAdmin(admin.ModelAdmin):
#    prepopulated_fields = {"slug": [slugify("titulo")]}


admin.site.register(Topico, TopicoAdmin)
admin.site.register(Entrada)
