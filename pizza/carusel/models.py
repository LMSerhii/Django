from django.db import models
from django.urls import reverse


class CmsSlider(models.Model):
    sl_img = models.ImageField(upload_to='sliderimg/', verbose_name='Зображення слайдера')
    sl_title = models.CharField(max_length=100, verbose_name='Заголовок слайдера')
    sl_text = models.CharField(max_length=250, verbose_name='Текст слайдера')
    sl_css = models.CharField(max_length=50, null=True, default='-', verbose_name='CSS класс')

    def __str__(self):
        return self.sl_title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайди'

    def get_absolute_url(self):
        return reverse('category', kwargs={'slide_id': self.pk})
