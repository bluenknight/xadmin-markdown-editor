# -*- encoding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=30,verbose_name=u'文章标题')
    content = models.TextField(verbose_name=u'文章内容')

    class Meta:
        verbose_name = u'文章管理'
        verbose_name_plural= verbose_name