from django.apps import AppConfig

class PollsConfig(AppConfig):
    name = 'polls' # path a nuestra app

    def ready(self): # Sobreescribimos el metodo ready de AppConfig
        import polls.signals # Importamos las señales de la app polls