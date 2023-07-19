from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

from .models import CmsSlider


class CmsAdmin(admin.ModelAdmin):
    list_display = ('sl_title', 'sl_text', 'sl_css', 'get_img')
    list_display_links = ('sl_title',)
    list_editable = ('sl_css',)
    fields = ('sl_title', 'sl_text', 'sl_css', 'sl_img', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        """ Возвращает форматированую html строку """
        if obj.sl_img:
            return mark_safe(f'<img src="{obj.sl_img.url}" width="180px"/>')
        else:
            return 'Порожньо'

    get_img.short_description = 'Мініатюра'


admin.site.register(CmsSlider, CmsAdmin)


