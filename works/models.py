# -*-coding: utf-8-*-
from django.db import models
from django.contrib.sites.models import Site
import datetime
from sorl.thumbnail import ImageField
import os.path

class Work(models.Model):
    seo_title = models.CharField(max_length=500, help_text="Заголовок (Для браузеров)", blank=True)
    seo_descritption = models.TextField(help_text="Описание (Для браузеров)", blank=True)
    seo_keywords = models.TextField(help_text="Ключевые слова (Для браузеров)", blank=True)

    logo = ImageField(upload_to='files', blank=True)
    poster = ImageField(upload_to='files')

    arch = models.BooleanField("Архив", default=False, help_text="Отправить это говно в архив!")

    slug = models.SlugField(unique=True, help_text="ссылка")
    title = models.CharField(max_length=500, help_text="Заголовок")
    content = models.TextField(help_text="Контент")

    date = models.DateTimeField(default=datetime.datetime.now)

    def get_absolute_url(self):
        return 'http://%s/works/%s/' % (Site.objects.get_current().domain, self.slug)

    def get_description(self):
        return self.content.split("<!--more-->")[0]

    def get_content(self):
        return self.content.split("<!--more-->")[1]

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date']


class WorkImage(models.Model):
    title = models.CharField(max_length=500, help_text="Заголовок")
    image = ImageField(upload_to='files', blank=True)
    desc = models.TextField(help_text="Описание", blank=True)
    parent = models.ManyToManyField('works.Work', null=True, help_text="Работа", blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Картинка"