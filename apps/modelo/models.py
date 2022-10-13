from pyexpat import model
from django.db import models


class Marca(models.Model):
    nombre = models.CharField(max_length=60, verbose_name='Marca')

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=60, verbose_name='Modelo')
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)


    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"

    def __str__(self):
        return '%s %s' % (self.marca, self.nombre)
