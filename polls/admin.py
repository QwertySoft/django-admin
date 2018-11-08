from django.contrib import admin
from polls.models import Question # Importamos el modelo Question

@admin.register(Question) # Registramos el admin del modelo Question
class QuestionAdmin(admin.ModelAdmin): # Definimos el admin del modelo Question que extiende de admin.ModelAdmin
    list_display = ('name', 'pub_date')
    search_fields = ('name',)
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'