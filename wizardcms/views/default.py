from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.cache import cache_page, never_cache
from netwizard.django.helpers import expose
from netwizard.core import manager
from netwizard.django.search import IGlobalSearch


@cache_page(10)
@expose('wizardcms/index.html')
def homepage(request):
    return {}

@never_cache
@expose('wizardcms/global_search.html')
def global_search(request, keyword=None):
    searchers = manager.find_extensions(IGlobalSearch)
    keyword = keyword or request.GET.get('keyword')
    request.session['wizardcms.search.keyword'] = keyword
    if keyword:
	    results = [(s.title, s.keyword_search(keyword)) for s in searchers]
    else:
        results = None
    return {
            'results': results,
            }
    