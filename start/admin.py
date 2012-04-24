# -*- coding: utf-8 -*-
from django.contrib import admin
from start.models import IndexPage

class IndexPageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('pos',)
        }),
        ('Содержимое', {
            'fields': ('menu', 'title', 'slug', 'content')
        }),
        ('сео', {
            'fields': ('seo_title', 'seo_descritption', 'seo_keywords')
        })
    )

admin.site.register(IndexPage, IndexPageAdmin)