# coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from article.models import Article, Tag, Classification
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.syndication.views import Feed  # 订阅RSS
import json
from django.core import serializers


# Create your views here.
def company_home(request):
	return render_to_response('demo/index.html', locals(), context_instance=RequestContext(request))