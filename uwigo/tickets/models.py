from django.utils.translation import gettext_lazy as _
from django.db import models

class Ticket(models.Model):

    class States(models.TextChoices):
        OPEN = 'OP', _('Abierto')
        PENDING = 'PD', _('Pendiente')
        IN_PROCESS = 'IP', _('En proceso')
        RESOLVE = 'RS', _('Resuelto')
        CLOSE = 'CL', _('Cerrado')
   

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    state = models.CharField(
        max_length=2,
        choices=States.choices,
        default=States.OPEN,
    )
    create_date = models.DateTimeField('Fecha de creación', auto_now=True)
