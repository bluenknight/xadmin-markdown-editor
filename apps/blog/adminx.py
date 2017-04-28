# -*- encoding:utf-8 -*-
import xadmin
from django import forms
from pagedown.widgets import AdminPagedownWidget

from .models import Article

class ArticleForm(forms.ModelForm):
	content = forms.CharField(widget=AdminPagedownWidget())
	class Meta:
		model = Article
		fields = '__all__'


class ArticleAdmin(object):
	form = ArticleForm


xadmin.site.register(Article,ArticleAdmin)
