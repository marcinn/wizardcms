"""
wizardCMS default models
"""

import os
import datetime
# from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from utils import parse_tracwiki, get_menu_item_provider
from django.utils.html import linebreaks, escape
from django.utils.safestring import mark_safe, mark_for_escaping
from django.template.loader import get_template_from_string
from django.template import Context
from django.contrib.markup.templatetags.markup import markdown


def _dummy_processor(s):
    return s

PAGE_TEMPLATE, SECTION_TEMPLATE, CUSTOM_TEMPLATE = (1,2,3)
TEMPLATE_TYPES = (
        (PAGE_TEMPLATE, _('Page template')),
        (SECTION_TEMPLATE, _('Section template')),
        (CUSTOM_TEMPLATE, _('Custom template')),
    )

NEW, ASSIGNED, INWORK, PROOF, ACCEPTED, PUBLISHED = (0, 2, 4, 6, 8, 10)

NODE_STATUSES = (
        (NEW, _('New')),
        (ASSIGNED, _('Assigned')),
        (INWORK, _('In work')),
        (PROOF, _('Proof-reading')),
        (ACCEPTED, _('Accepted')),
        (PUBLISHED, _('Published')),
    )

MARKUP_WIKI = 'W'
MARKUP_MARKDOWN = 'M'
MARKUP_PLAIN = 'P'
MARKUP_HTML = 'H'

MARKUPS = (
        (MARKUP_PLAIN, _('Plain text')),
        (MARKUP_WIKI, _('Wiki markup')),
        (MARKUP_MARKDOWN, _('Markdown')),
        (MARKUP_HTML, _('HTML code')),
        )

MARKUP_PROCESSORS = dict((
        (MARKUP_HTML, _dummy_processor),
        (MARKUP_WIKI, parse_tracwiki),
        (MARKUP_MARKDOWN, markdown),
        (MARKUP_PLAIN, (linebreaks, escape)),
        ))


class Language(models.Model):
    """ holds defined languages """
    name = models.CharField(max_length=64, verbose_name=_('name'))
    is_active = models.BooleanField(default=False, verbose_name=_('is active'))

    class Meta:
        verbose_name = _('language')
        verbose_name_plural = _('languages')

    def __unicode__(self):
        return self.name

class TemplateManager(models.Manager):
    def custom(self):
        return self.get_query_set().filter(type=CUSTOM_TEMPLATE)


class Template(models.Model):
    """ user-defined templates """
    type = models.IntegerField(choices=TEMPLATE_TYPES)
    name = models.CharField(max_length=64, verbose_name=_('name'))
    path = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('path'))
    content = models.TextField(verbose_name=_('content'))
    objects = TemplateManager()

    class Meta:
        verbose_name = _('template')
        verbose_name_plural = _('templates')

    def __unicode__(self):
        return self.name


class NodeManager(models.Manager):
    def roots(self):
        return self.get_query_set().filter(parent=None)
    def get_query_set(self):
        return super(NodeManager, self).get_query_set().order_by('display_order')


class Node(models.Model):
    """ a sitemap node model """
    language = models.ForeignKey(Language, verbose_name=_('language'))
    parent = models.ForeignKey('self', null=True, blank=True, related_name="child_nodes", verbose_name=_('parent node'))
    status = models.IntegerField(choices=NODE_STATUSES)
    title = models.CharField(max_length=255, verbose_name=_('title'))
    short_title = models.CharField(max_length=64, null=True, blank=True, verbose_name=_('short title'))
    slug = models.SlugField(unique=True, max_length=255, null=True, blank=True, help_text=_('Type here unique alias for page. Use only small letters, underscore and digits'), verbose_name=_('slug'))
    meta_description = models.TextField(max_length=160, null=True, blank=True, verbose_name=_('meta description'))
    meta_keywords = models.TextField(max_length=255, null=True, blank=True, verbose_name=_('meta keywords'))
    meta_author = models.CharField(max_length=64, null=True, blank=True, verbose_name=_('meta author'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateField(auto_now_add=True, auto_now=True, verbose_name=_('updated at'))
    content_type = models.ForeignKey(ContentType)
    content_object = generic.GenericForeignKey('content_type', 'id')
    display_order = models.PositiveIntegerField(default=0)
    objects = NodeManager()


    class NodeNavigationPath(list):

        def titles(self):
            return [n.title for n in self]

        def identifiers(self):
            return [n.id for n in self]

        def __unicode__(self):
            path_s = [n.title for n in self]
            return ' > '.join(path_s)


    def get_is_published(self):
        """ returns true, if Node is published """
        return self.status == PUBLISHED
    get_is_published.boolean = True

    def __unicode__(self):
        return self.title

    def has_children(self):
        return self.child_nodes.count()>0

    def get_navigation_path(self):
        item = self
        path = self.NodeNavigationPath([self])
        while item.parent:
            item = item.parent
            path.append(item)
        path.reverse()
        return path
    get_navigation_path.short_description = _('Navigation')
    # get_navigation_path.admin_order_field = 'parent'

    def language_name(self):
        return self.language.name

    def save(self, force_insert=False, force_update=False):
        if not self.slug:
            parts = self.get_navigation_path().titles()
            parts.append(self.slug.split('-')[-1])
            parts = [h.slugify(p) for p in parts if p]
            self.slug = '-'.join(parts)
            # self.slug = h.slugify(self.title)

        if not self.content_type_id:
            self.content_type = ContentType.objects.get_for_model(self.__class__)
            super(Node, self).save(force_insert=force_insert, force_update=force_update)

        return super(Node, self).save(force_insert,force_update)

    is_published = property(get_is_published)
    

class Category(models.Model):
    symbol = models.CharField(max_length=64)
    name = models.CharField(max_length=255, verbose_name=_('name'))
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('description'))

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __unicode__(self):
        return self.name or self.symbol


class PageQuerySet(models.query.QuerySet):
    def published(self):
        return self.filter(status=PUBLISHED)
    def accepted(self):
        return self.filter(status=ACCEPTED)
    def in_work(self):
        return self.filter(status=INWORK)
    def in_proof_reading(self):
        return self.filter(status=PROOF)
    def new(self):
        return self.filter(status=NEW)
    def assigned(self):
        return self.filter(status=ASSIGNED)
    def last_added(self):
        return self.order_by('-post_date')


class PageManager(NodeManager):
    use_for_related_fields = True
    def get_query_set(self):
        return PageQuerySet(self.model).order_by('display_order')

    def published(self):
        return self.get_query_set().published()

class Page(Node):
    """ is a sitemap node concrete element, that holds sections with content """
    publish_from = models.DateField(null=True, blank=True, help_text=_('Set optional publication period'), verbose_name=_('publish from'))
    publish_to   = models.DateField(null=True, blank=True, verbose_name=_('publish to'))
    template = models.ForeignKey(Template, limit_choices_to={'type': PAGE_TEMPLATE}, null=True, blank=True, verbose_name=_('template'))
    introduction = models.TextField(blank=True, null=True, verbose_name=_('introduction'))
    description = models.TextField(blank=True, null=True, verbose_name=_('description'))
    post_date = models.DateField(null=True, verbose_name=_('post date'))
    category = models.ForeignKey(Category, related_name='pages', null=True, blank=True, verbose_name=_('category'))
    photo = models.ImageField(max_length=255, null=True, blank=True,
            upload_to=os.path.join('uploads','pages'), verbose_name=_('page photo'),)
    objects = PageManager()

    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')

#    def child_nodes(self):
#        return self.__class__.objects.filter(parent=self)
    
    def get_is_published(self):
        """ 
        returns True, if Page is published
        overloaded Node model method
        """
        return not (self.publish_from and self.publish_to) and self.is_published
    get_is_published.short_description = _('is published')
    
    def intro(self):
        if self.introduction:
            return self.introduction
        if self.pagesection_set.count():
            return self.pagesection_set.all()[0].content[:200]
        return ''

    def image(self):
        if self.photo:
            return self.photo
        return self.section_image()

    def section_image(self):
        if self.pagesection_set.count():
            return self.pagesection_set.all()[0].image_path
        return None

    def sections(self):
        return self.pagesection_set.all()

    @property
    def children(self):
        return self.__class__.objects.filter(parent=self)


class PageSectionManager(models.Manager):
    def get_query_set(self):
        return super(PageSectionManager, self).get_query_set().order_by('display_order')


class PageSection(models.Model):
    """ a part of page with own image, content, title and template """
    page = models.ForeignKey(Page)
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('title'))
    content = models.TextField(blank=True, verbose_name=_('content'))
    image_path = models.ImageField(
            max_length=255, 
            null=True, 
            blank=True,
            upload_to=os.path.join('uploads','pages'),
            verbose_name=_('image path'),
        )
    template = models.ForeignKey(Template, limit_choices_to={'type': SECTION_TEMPLATE}, verbose_name=_('template'))
    display_order = models.PositiveIntegerField(blank=True, verbose_name=_('display order'))
    markup = models.CharField(max_length=1, choices=MARKUPS, default=MARKUP_WIKI, verbose_name=_('text format'))
    objects = PageSectionManager()

    class Meta:
        verbose_name = _('section')
        verbose_name_plural = _('sections')

    def save(self, force_insert=False, force_update=False):
        if not self.display_order:
            self.display_order = self.page.pagesection_set.all().count() + 1
        return super(PageSection, self).save(force_insert,force_update)

    @property
    def as_html(self):
        markups = dict(MARKUP_PROCESSORS)
        content = markups[self.markup](self.content)
        return get_template_from_string(self.template.content).render(Context({'title': self.title, 'content': content}))



class PageAttachmentManager(models.Manager):
    #    use_for_related_fields = True
    
    def published(self):
        return self.get_query_set().filter(is_published=True)

class PageAttachment(models.Model):
    """ holds page attachments (files, documents) """
    page = models.ForeignKey(Page, related_name='attachments')
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('name'))
    file_path = models.FileField(
            max_length=255, 
            upload_to=os.path.join('uploads','attachments'),
            verbose_name=_('file path')
        )
    is_published = models.BooleanField(default=False, verbose_name=_('is published'))
    objects = PageAttachmentManager()
    
    class Meta:
        verbose_name = _('attachment')
        verbose_name_plural = _('attachments')

    def __unicode__(self):
        return self.name or self.file_path

class MenuManager(models.Manager):
    def published(self):
        return self.filter(is_published=True)


class Menu(models.Model):
    """ 
    menu holds many items (nodes)
    holds nodes from different sitemap levels into one group
    """
    symbol = models.CharField(max_length=32)
    language = models.ForeignKey(Language, verbose_name=_('language'))
    name = models.CharField(max_length=64, verbose_name=_('name'))
    is_published = models.BooleanField(default=False, verbose_name=_('is published'))
    objects = MenuManager()

    class Meta:
        """ meta info for Menu model """
        unique_together = (('symbol','language'),)
        verbose_name = _('menu')
        verbose_name_plural = _('menus')

    def __unicode__(self):
        return self.name

    @property
    def published_items(self):
        return self.items.published()


class MenuItemManager(models.Manager):
    def get_query_set(self):
        return super(MenuItemManager, self).get_query_set().order_by('display_order')

    def published(self):
        return self.get_query_set().filter(is_published=True)


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items')
    display_order = models.PositiveIntegerField(verbose_name=_('display order'))
    type = models.CharField(max_length=32, verbose_name=_('type'))
    value = models.CharField(max_length=255, verbose_name=_('value'))
    is_published = models.BooleanField(default=False, verbose_name=_('is published'))
    title = models.CharField(max_length=255, default='', blank=True, verbose_name=_('title'))
    objects = MenuItemManager()

    class Meta:
        verbose_name = _('menu item')
        verbose_name_plural = _('menu items')

    def __unicode__(self):
        return '%s: %s' % (self.type, self.target)

    @property
    def target(self):
        return get_menu_item_provider(self.type).get_object(self.value)

    @property
    def url(self):
        return get_menu_item_provider(self.type).get_url(self.value)

    @property
    def short_title(self):
        return self.title

    def save(self, force_insert=False, force_update=False):
        # autogenerate display order
        if not self.display_order:
            # change it to max(menu_id)+1 when
            # django will be support agregate funcs in stable version
            self.display_order = MenuItem.objects.filter(menu=self.menu).count()+1
        return super(MenuItem, self).save(force_insert=force_insert, force_update=force_update)


