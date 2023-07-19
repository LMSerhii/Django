from django.apps import AppConfig
from django.urls import reverse


class CaruselConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carusel'
    verbose_name = 'Слайдер'
