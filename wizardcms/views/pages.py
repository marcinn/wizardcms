from django.http import Http404
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.cache import cache_page, never_cache
from django.template.loader import get_template_from_string, get_template
from wizardcms import models
from django.utils.translation import ugettext as _
from django.template import TemplateSyntaxError
from django.views.generic.list_detail import object_list, object_detail


class PageTemplateLoader(object):
    def get_template(self, template_model=None):
        if isinstance(template_model, str):
            return get_template(template_model)
        if template_model:
            try:
                return get_template_from_string(template_model.content)
            except TemplateSyntaxError, e:
                if settings.TEMPLATE_DEBUG:
                    return get_template_from_string(
                            _('Cannot render page template "%(name)".\
                               Please correct template errors: %(errors)'
                               % {'name':template_model.name, 'errors': e}))

page_template_loader = PageTemplateLoader()

@cache_page(10)
def list(request, category_id=None, name=None, extra_context=None, template_name=None, queryset=None):
    queryset = queryset or models.Page.objects.published().select_related()
    if category_id:
        queryset = queryset.filter(parent=category_id)
    return object_list(request, queryset=queryset,
            template_name=template_name or 'wizardcms/pages/list.html',
            paginate_by=20, template_object_name='page')

@cache_page(10)
def show(request, id=None, extra_context=None, queryset=None, slug=None):
    queryset = queryset or models.Page.objects.published()
    try:
        if id:
            page = queryset.get(id=id)
        elif slug:
            page = queryset.get(slug=slug)
    except models.Page.DoesNotExist:
        raise Http404
    return object_detail(request, queryset=queryset,
            object_id=id, slug=slug, template_loader=page_template_loader,
            template_name=page.template or 'wizardcms/pages/view.html',
            template_object_name='page')

def listslug(request, slug):
    return list(request, queryset=models.Node.objects.filter(slug=slug))

def viewslug(request, slug):
    return show(request, slug=slug)
