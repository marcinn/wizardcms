from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('wizardcms.views',
        url(r'search/(.+)/$', 'default.global_search', name='wizardcms-globalsearch'),
        url(r'search/?P<keyword>(.+)/$', 'default.global_search', name='wizardcms-globalsearch'),
        url(r'search/$', 'default.global_search', name='wizardcms-globalsearch'),
        url(r'page/(\d+).html$', 'pages.show', name='wizardcms-page-view'),
        url(r'page/(\d+),([a-z0-9-]+).html$', 'pages.show', name='wizardcms-page-view'),
        url(r'(?P<slug>[a-z]+[a-z0-9-\/]+).html$', 'pages.viewslug', name='wizardcms-page-view'),
        url(r'([a-z]+[a-z0-9-]+)/$', 'pages.listslug', name='wizardcms-page-list'),
        url(r'pages/(\d+)/$', 'pages.list', name='wizardcms-page-list'),
        url(r'^$', 'default.homepage', name='wizardcms-homepage'),
        )

