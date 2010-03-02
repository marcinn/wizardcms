from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.cache import cache_page, never_cache


def global_search(request, keyword=None, extra_context=None):
    pass
