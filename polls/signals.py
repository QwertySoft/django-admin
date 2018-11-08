from django.db.models.signals import post_save # Importamos post_save
from django.dispatch import receiver # Importamos receiver
from polls.models import Question # Importamos el modelo Question

@receiver(post_save, sender=Question) # Decoramos el manejador para que se ejecute cuando una pregunta se guarde
def my_handler(sender, instance, **kwargs): # Definimos el manejador
    print(sender) # Imprimimos el sender
    print(instance) # Imprimimos la instancia que se acaba de guardar
    print('La pregunta acaba de guardarse con ID = {}'.format(instance.id)) # Imprimimos el ID de la pregunta persistida