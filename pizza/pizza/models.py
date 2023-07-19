from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категорія')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категорії'
        ordering = ['id', ]

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


class Pizza(models.Model):
    title = models.CharField(max_length=100, verbose_name='Назва')
    ingredients = models.CharField(max_length=255, verbose_name='Інгредієнти')
    description = models.TextField(null=True)
    photo = models.ImageField(upload_to='pizzas', verbose_name='Фото')
    price = models.CharField(max_length=100, verbose_name='Ціна')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name='Категорія')

    class Meta:
        verbose_name = 'Піцу'
        verbose_name_plural = 'Піца'
        ordering = ['-time_create']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pizza', kwargs={'pizza_id': self.pk})

