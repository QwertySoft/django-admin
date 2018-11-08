from django.db import models
from django.utils.timezone import now

class Question(models.Model):
    name = models.CharField('Nombre', max_length=255, blank=True, null=True)
    pub_date = models.DateTimeField('Fecha de publicacion', blank=True, null=True, default=now)

    class Meta:
        ordering = ['id', '-pub_date']

    def __str__(self):
        return 'Pregunta: {}'.format(self.name)