from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class MyWorksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_works'
    verbose_name = _('My Works')


    def ready(self):
        import my_works.signals
   
