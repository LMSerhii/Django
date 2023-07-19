from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'get_img', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_editable = ('price', 'category', 'is_published')
    list_filter = ('is_published', 'category')

    def get_img(self, obj):
        """ Возвращает форматированую html строку """
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="180px"/>')
        else:
            return 'Порожньо'

    get_img.short_description = 'Мініатюра'


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Category)
