from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('pizza/', pizza, name='pizza'),
    path('location/', location, name='location'),
    path('about/', about, name='about'),
    path('delivery/', delivery, name='delivery'),
    path('contacts/', contacts, name='contacts'),
    path('login/', login, name='login'),


]