from django.shortcuts import render
from .models import *
from carusel.models import *


def pageNotFound(request, exception):
    return render(request, 'pizza/page404.html')


def index(request):
    pizzas = Pizza.objects.all()
    slide_list = CmsSlider.objects.all()

    context = {
        'title': 'Головна сторінка',
        'pizzas': pizzas,
        'slide_list': slide_list,

    }
    return render(request, 'pizza/index.html', context=context)


def pizza(request, pizza_id):
    pizza_item = Pizza.objects.get(pk=pizza_id)
    context = {
        'title': pizza_item.title,
        'pizza': pizza_item
    }
    return render(request, 'pizza/pizza.html', context=context)


def location(request):
    context = {
        'title': 'Локація',
    }
    return render(request, 'pizza/index.html', context=context)


def about(request):
    context = {
        'title': 'Про нас',
    }
    return render(request, 'pizza/index.html', context=context)


def delivery(request):
    context = {
        'title': 'Доставка та оплата',
    }
    return render(request, 'pizza/index.html', context=context)


def contacts(request):
    context = {
        'title': 'Контакти',
    }
    return render(request, 'pizza/index.html', context=context)


def login(request):
    context = {
        'title': 'Авторизація',
    }
    return render(request, 'pizza/index.html', context=context)
