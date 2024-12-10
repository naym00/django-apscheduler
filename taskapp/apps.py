from django.apps import AppConfig


class TaskappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'taskapp'

    def ready(self):
        from taskapp.auto_task import script
        script.start()