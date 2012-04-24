# -*- coding: utf-8 -*-
from django.contrib import admin
from team.models import Person

class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('pos', 'photo')
        }),
        ('Содержимое', {
            'fields': ('name', 'desc')
        })
    )