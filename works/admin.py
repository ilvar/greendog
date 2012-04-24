# -*- coding: utf-8 -*-
from django.contrib import admin
from sorl.thumbnail import default
from works.models import Work, WorkImage

ADMIN_THUMBS_SIZE = '100x100'

class WorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('arch', 'date', 'logo', 'poster')
        }),
        ('Содержимое', {
            'fields': ('title', 'slug','content')
        }),
        ('сео', {
            'fields': ('seo_title', 'seo_descritption', 'seo_keywords')
        })
    )

class WorkImageAdmin(admin.ModelAdmin):
    def image_display(self, obj):
        thumb = default.backend.get_thumbnail(obj.image.file, ADMIN_THUMBS_SIZE)
        return '<img src="%s" width="%s" />' % (thumb.url, thumb.width)
    image_display.allow_tags = True

    filter_horizontal = ('parent',)

    fieldsets = (
        (None, {
            'fields': ('image', 'title', 'desc')
        }),
        (None, {
            'fields': ('parent',)
        }),
    )

    list_display = ('title', 'image_display')
    list_per_page = 10

admin.site.register(WorkImage, WorkImageAdmin)
admin.site.register(Work, WorkAdmin)