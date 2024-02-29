from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from hashid_field import HashidAutoField


# Create your models here.
class Topico(models.Model):
    topico = models.CharField(max_length=100)
    adicionado_em = models.DateField(auto_now_add=True)
    editado_em = models.DateField(auto_now=True)
    slug = models.SlugField(default="", null=False, unique=False)
    dono = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "tópico"
        verbose_name_plural = "tópicos"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.topico)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("entradas", kwargs={"slug_topico": self.slug})

    def __str__(self):
        return self.topico


class Entrada(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    id = HashidAutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    adicionada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"

    def get_absolute_url(self):
        return reverse("entradas", kwargs={"slug_topico": self.topico.slug})

    def __str__(self):
        if len(self.texto) > 50:
            return self.texto[:50] + "..."
        else:
            return self.texto
