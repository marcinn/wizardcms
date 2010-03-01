import models
import logging
from netwizard.core import manager

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


def get_all_menu_item_providers():
    from plugins import IMenuItemTypeProvider
    return manager.find_extensions(IMenuItemTypeProvider)

def get_menu_item_provider(symbol):
    qs = [provider for provider in get_all_menu_item_providers() if symbol == provider.symbol ]
    if qs:
        return qs[0]
    return None


