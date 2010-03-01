"""
WizardCMS plugins API
"""

import exceptions
from netwizard.core import Component, Interface, ComponentMeta, manager
from django.core.urlresolvers import reverse
from django import template 
from netwizard.django.search import IGlobalSearch
from wizardcms import models 
from django.db.models import Q

"""
plugins abstract
"""

class MenuItemProviderMeta(ComponentMeta):
    def __init__(cls, name, bases, dct):
        if not cls.__name__ == 'BaseMenuItemProvider':
            if not cls.symbol:
                cls.symbol = cls.__name__
            #if cls.symbol in [inst.symbol for inst in get_all_menu_item_providers()]:
            #    raise exceptions.NameError('%s provider name conflict (already exists), provided by %s' % (cls.symbol, cls.__name__))

        super(MenuItemProviderMeta, cls).__init__(name, bases, dct)


class IMenuItemTypeProvider(Interface):
    abstract = True
    symbol = None

    def get_url(self, value):
        raise exceptions.NotImplemented

    def get_admin_url(self, value):
        raise exceptions.NotImplemented

    def get_select_widget(self, value):
        raise exceptions.NotImplemented

    def get_object(self, value):
        raise exceptions.NotImplemented


class BaseMenuItemProvider(Component, IMenuItemTypeProvider):
    abstract = True
    __metaclass__ = MenuItemProviderMeta


"""
Default menu item providers
"""

class PageMenuItem(BaseMenuItemProvider):
    def get_url(self, value):
        page = models.Page.objects.get(id=value)
        if page.slug:
            return reverse('wizardcms-page-view', kwargs={'slug': page.slug,})
        return reverse('wizardcms-page-view', args=[value])

    def get_select_widget(self, value):
        return None

    def get_admin_url(self, value):
        return '#'

    def get_object(self, value):
        try:
            obj = models.Page.objects.get(id=value)
            obj.url = self.get_url(value) # zostawic tak ?
            return obj
        except models.Page.DoesNotExist:
            return None


class Url(BaseMenuItemProvider):
    def get_url(self, value):
        return value

    def get_admin_url(self, value):
        return value

    def get_object(self, value):
        class _urlwrapper(object):
            def __init__(self, title, url):
                self.short_title = title
                self.url = url
                self.id = None
                self.title = url
        return _urlwrapper(value, value)


"""
Dashboard
"""

try:
    from antymedia.antyadmin.admin import site

    class CmsSummary(object):
        title = "Podsumowanie CMS"
        def render(self):
            data = {
                    'pages': {
                        'published': models.Page.objects.all().published().count(),
                        'overall':  models.Page.objects.all().count(),
                        'in_work': models.Page.objects.all().in_work().count(),
                        'proof_reading': models.Page.objects.all().in_proof_reading().count(),
                        'accepted': models.Page.objects.all().accepted().count(),
                        'new': models.Page.objects.all().new().count(),
                        'assigned': models.Page.objects.all().assigned().count(),
                        },
                    }
            return template.loader.render_to_string(
                    'wizardcms/dashboard/summary.html', 
                    data)
            
except ImportError:
    pass

class PageSearch(IGlobalSearch, Component):
    title = "Wyniki wyszukiwania stron"
    def keyword_search(self, keyword):
        ps_query = Q(content__icontains=keyword) \
                | Q(title__icontains=keyword)
        pg_query = Q(title__icontains=keyword) \
                | Q(short_title__icontains=keyword)
        pages = list(models.PageSection.objects.filter(ps_query).values_list('page_id', flat=True))
        pages = pages + list(models.Page.objects.filter(pg_query).values_list('id', flat=True))
        result = models.Page.objects.published().filter(pk__in=pages)
        return [(ps.page.title, reverse('wizardcms-page-view',args=[ps.page.id])) for ps in result[:10]]
    def search(self, **kwargs):
        pass
    
