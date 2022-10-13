from enum import auto
from pyexpat import model
from tabnanny import verbose
from django.db import models

from apps.auto.models import Auto

class Mantenimiento(models.Model):
    kilometraje = models.PositiveSmallIntegerField(verbose_name='Kilometraje')
    descripcion = models.CharField(verbose_name='Descripción', max_length=250)
    costo = models.PositiveSmallIntegerField(verbose_name='Costo')
    fecha = models.DateTimeField(verbose_name='Fecha y hora')
    auto = models.ForeignKey(Auto, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'

    def __str__(self):
        return '%s: %s' % (self.auto, self.fecha)
