from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizzas'
    
    
    def __str__(self):
        return self.name
    
    
class Topping(models.Model):
    pizza = models.ManyToManyField(Pizza)
    name = models.CharField(max_length=200)
    
    class Meta:        
        verbose_name = 'Topping'
        verbose_name_plural = 'Toppings'
        
    def __str__(self):
        return self.name
    
    
    

    
    
