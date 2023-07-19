from django.shortcuts import render
from .models import Pizza, Topping


def index(request):
    title = 'Pizza'
    context = {'title': title}
    return render(
        request=request,
        template_name='pizzas/index.html',
        context=context
        )
    
def pizzas(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    
    return render(
        request=request,
        template_name='pizzas/pizzas.html',
        context=context
                  )
    
def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza': pizza, 'toppings': toppings }
    
    return render(
        request=request,
        template_name='pizzas/pizza.html',
        context=context
                  )