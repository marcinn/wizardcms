# -*- coding: utf-8 -*-
import models
import logging
import re
import unicodedata

try:
    from trac.test import EnvironmentStub, Mock, MockPerm 
    from trac.mimeview import Context 
    from trac.wiki.formatter import HtmlFormatter 
    from trac.web.href import Href
    env = EnvironmentStub() 
    req = Mock(href=Href('/'), abs_href=Href('http://www.example.com/'), 
               authname='anonymous', perm=MockPerm(), args={})
    context = Context.from_request(req, 'wiki')
    def parse_tracwiki(s):
        return HtmlFormatter(env, context, s).generate()

    from tracutils import tracmacros

except ImportError:
    def parse_tracwiki(s):
        return s
    logging.warning('Trac packages not found - disabling Trac wiki markup')


from django.template import TemplateDoesNotExist

def load_template_source(template_name, template_dirs=[]):
    try:
        template = models.Template.objects.custom().get(path=template_name)  
        return (template.content, None)
    except models.Template.DoesNotExist:
        raise TemplateDoesNotExist
load_template_source.is_usable=True


__re_slugify__ = re.compile('[^\w-]+')

def slugify(string):
    """
    transform input string to slug-like value
    (no spaces, lowercase, no lang-specific chars)
    """
    slug = unicodedata.normalize('NFKD', 
             unicode(string.lower())
             .replace(u'ł','l')
             .replace(u'Ł','L')
           ).encode('ascii','ignore').lstrip().rstrip()
    return __re_slugify__.sub('-', slug)




