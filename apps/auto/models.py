from django.db import models
from apps.modelo.models import Modelo

from apps.user.models import User

class Auto(models.Model):
    placa = models.CharField(verbose_name='Placa', max_length=10)
    kilometraje = models.PositiveSmallIntegerField(verbose_name='Kilometraje') #Actualizar al guardar unmantenimiento
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Autos'

    def __str__(self):
        return '%s, %s' % (self.modelo, self.placa)
