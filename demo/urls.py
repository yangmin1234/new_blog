#coding:utf-8
from django.conf.urls import patterns, include, url
from views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^company_home/$', company_home, name="company_home"),
)
