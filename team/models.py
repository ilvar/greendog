# -*-coding: utf-8-*-
from django.db import models
from sorl.thumbnail import ImageField
import os.path

class Person(models.Model):
    name = models.CharField(max_length=500, help_text="Имя")
    desc = models.TextField(help_text="Пост")
    photo = ImageField(upload_to='files', blank=True)

    pos = models.CharField(max_length=500, help_text="позиция")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['pos']
        verbose_name_plural = "Люди"
