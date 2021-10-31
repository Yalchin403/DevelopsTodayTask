from django.apps import AppConfig


# class BackendConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'backend'


class BackendConfig(AppConfig):
    name = "backend"

    def ready(self):
        import backend.tasks
