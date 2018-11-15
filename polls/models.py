# Importamos los móculos que necesitamos
from django.db import models

# Definimos el modelo Question
class Question(models.Model):
    # Definimos los campos del modelo Question
    name = models.CharField('Nombre', max_length=10, blank=False, null=False, default='')
    pub_date = models.DateTimeField('Fecha de publicación', blank=True, null=True, auto_now_add=True)

    # Definimos la clase Meta para el modelo Question
    class Meta:
        # Definimos el orden por defecto al recuperar el listado de preguntas
        ordering = ['id', '-pub_date']

    # Implementamos el método __str__
    def __str__(self):
        return 'Pregunta: {}'.format(self.name)