from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """  """
    text = models.CharField(max_length=200, verbose_name='Текст')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')

    def __str__(self):
        """ """
        return self.text

    class Meta:
        verbose_name = 'Тему'
        verbose_name_plural = 'Темы'


class Entry(models.Model):
    """"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текстовое поле')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return f"{self.text[:50]}..."

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'

