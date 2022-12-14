from django.utils.translation import gettext_lazy as _
from django.db import models
from django import forms

class Ticket(models.Model):

    class Meta:
        permissions = (("can_create", "Crear un ticket"),)


    class States(models.TextChoices):
        OPEN = 'OP', _('Abierto')
        PENDING = 'PD', _('Pendiente')
        IN_PROCESS = 'IP', _('En proceso')
        RESOLVE = 'RS', _('Resuelto')
        CLOSE = 'CL', _('Cerrado')
   
    title = models.CharField('Titulo',max_length=100)

    description = models.CharField('Descripción', max_length=500)
    state = models.CharField(verbose_name='Estado',
        max_length=2,
        choices=States.choices,
        default=States.OPEN,
    )
    create_date = models.DateTimeField('Fecha de creación', auto_now=True)

    