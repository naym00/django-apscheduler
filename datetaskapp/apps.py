from django.apps import AppConfig


class DatetaskappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'datetaskapp'

    def ready(self):
        from datetaskapp.auto_task import script
        script.start()
