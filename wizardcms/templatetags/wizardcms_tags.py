from django.utils.safestring import mark_safe, mark_for_escaping
from django import template
from wizardcms.utils import parse_tracwiki
from wizardcms.models import Page, Menu, MenuItem
from django.template import TemplateSyntaxError
from django.template.loader import get_template_from_string

register = template.Library()


@register.filter
def tracwiki(s):
    return mark_safe(parse_tracwiki(s))


register.filter('wikimarkup', tracwiki)


@register.inclusion_tag('admin/wizardcms/tree_navigation.html')
def wizardcms_pages_navigation(cl):
    from wizardcms.admin import NodeTreeNavigation
    return {
            'navigation': NodeTreeNavigation(cl.query_set.query.where, 'urltemplate'),
            }
    #    return mark_for_escaping(cl.query_set.query.where)

class SectionNode(template.Node):
    def __init__(self, section, cast_as=None):
        self.section = section
        self.cast_as = cast_as

    def render(self, context):
        section = self.section.resolve(context)
        context.push()
        context.update(section.__dict__) # copy whole section properties
        context['content'] = section._format_content()
        result = get_template_from_string(
                section.template.content).render(context)
        context.pop()
        if self.cast_as:
            context[self.cast_as] = result
            return ''
        return result


class PageListNode(template.Node):
    def __init__(self, slug, cast_as, **options):
        self.slug = slug
        self.cast_as = cast_as
        self.options = options
    
    def render(self, context):
        try:
            if self.slug:
                pages = Page.objects.published().get(slug=self.slug).children.published()
            else:
                pages = Page.objects.published()

            if self.options.has_key('category'):
                pages = pages.select_related().filter(category__symbol=self.options['category'])

            if self.options.has_key('sort'):
                if self.options['sort'] == 'last_added':
                    pages = pages.last_added()

            if self.options.has_key('limit'):
                pages = pages[:self.options['limit']]

            if self.options.get('noparent'):
                pages = pages.filter(parent=None)

            if self.cast_as:
                context[self.cast_as] = pages
                return ''
            return pages
        except Page.DoesNotExist:
            return ''


def _parse_options(bits):
    options = {}
    for arg in bits:
        if arg.find('=') == -1:
            # raise TemplateSyntaxError, "invalid tag options"
            options[str(arg)] = True
        else:
            try:
                argname, argval = arg.split('=')
                options[str(argname)] = argval
            except ValueError:
                raise TemplateSyntaxError, "invalid tag option \"%s\"" % str(arg)
    return options



@register.tag
def get_latest_pages(parser, token):
    bits = token.contents.split()
    if len(bits) <4 or len(bits) >5:
        raise TemplateSyntaxError, "%s tag takes at least three arguments" % bits[0]
    if bits[2] == 'as':
        slug = None
        limit = bits[1]
        cast_as = bits[3]
        rest = bits[4:]
    elif bits[3] == 'as':
        slug = bits[1]
        limit = bits[2]
        cast_as = bits[4]
        rest = bits[5:]
    else:
        raise TemplateSyntaxError, "%s invalid tag arguments" % bits[0]
    try:
        options = _parse_options(rest)
        options['limit'] = limit
        return PageListNode(slug, cast_as, **options)
    except TemplateSyntaxError, e:
        raise TemplateSyntaxError("%s tag error: %s" % (bits[0], e))


@register.tag
def get_pages(parser, token):
    bits = token.contents.split()
    if len(bits) <2:
        raise TemplateSyntaxError, "%s tag takes at least two arguments" % bits[0]

    if bits[1] == 'as':
        root = None
        cast_as = bits[2]
        rest = bits[3:]
    elif bits[2] == 'as':
        root = bits[1]
        cast_as = bits[3]
        rest = bits[4:]

    try:
        return PageListNode(root, cast_as, **_parse_options(rest))
    except TemplateSyntaxError, e:
        raise TemplateSyntaxError("%s tag error: %s" % (bits[0], e))




class MenuItemsNode(template.Node):
    def __init__(self, symbol, cast_as=None):
        self.symbol = symbol
        self.cast_as = cast_as

    def render(self, context):
        items = ''
        try: 
            items = MenuItem.objects.filter(menu__symbol=self.symbol)
        except Menu.DoesNotExist:
            pass
        finally:
            if self.cast_as:
                context[self.cast_as] = items
                return ''
            return items


@register.tag
def get_menu_items(parser, token):
    bits = token.contents.split()
    if len(bits) <2 or len(bits) >4:
        raise TemplateSyntaxError, "%s tag takes one or three arguments" % bits[0]

    if len(bits) == 2:
        return MenuItemsNode(bits[1])
    if not bits[2] == 'as':
        raise TemplateSyntaxError, "%s invalid tag argument" % bits[0]
    return MenuItemsNode(bits[1], bits[3])

    
@register.tag
def render_section(parser, token):
    bits = token.contents.split()
    if len(bits) <2 or len(bits) >3:
        raise TemplateSyntaxError, "%s tag takes one argument - section" % bits[0]
    return SectionNode(parser.compile_filter(bits[1]))

