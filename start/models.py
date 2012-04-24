# -*-coding: utf-8-*-
from django.db import models

class IndexPage(models.Model):
    seo_title = models.CharField(max_length=500, help_text="Заголовок (Для браузеров)", blank=True)
    seo_descritption = models.TextField(help_text="Описание (Для браузеров)", blank=True)
    seo_keywords = models.TextField(help_text="Ключевые слова (Для браузеров)", blank=True)

    pos = models.CharField(max_length=500, help_text="позиция")

    menu = models.CharField(max_length=500, help_text="")
    slug = models.SlugField(unique=True, help_text="ссылка")

    title = models.CharField(max_length=500, help_text="Заголовок")
    content = models.TextField(help_text="Контент")

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['pos']