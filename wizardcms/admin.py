from django.contrib import admin
from netwizard.django.apps.tabbed_admin import admin as tabadmin
from netwizard.django.apps.batchadmin import admin as batchadmin
from django.contrib.admin import site, options
from django.contrib.admin.util import quote, unquote, flatten_fieldsets, get_deleted_objects
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.forms.models import modelform_factory, ModelForm
from netwizard.core import manager as componentmgr
import forms
import models
import widgets

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'type',)
    list_filter = ('type',)
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(TemplateAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'content':
            field.widget = widgets.AdminTemplateEditWidget()
        return field


class MenuItemInline(admin.TabularInline):
    model = models.MenuItem
    extra = 1

class MenuAdmin(admin.ModelAdmin):
    inlines = (MenuItemInline,)
    list_display = ('symbol', 'name', 'language', 'is_published',)
    list_display_links = ('symbol', 'name', )
    list_filter = ('is_published', 'language',)
    search_fields = ('symbol', 'name',)



class PageSectionsFormset(options.BaseInlineFormSet):
    def get_queryset(self):
        qs = super(PageSectionsFormset, self).get_queryset()
        return qs.order_by('display_order')

class PageSectionInline(admin.StackedInline):
    model = models.PageSection
    extra = 1
    exclude = ('display_order',)
    formset = PageSectionsFormset

class PageAttachmentInline(admin.TabularInline):
    model = models.PageAttachment
    extra = 1

class NodeAdmin(tabadmin.TabbedModelAdmin):
    change_list_template = "admin/wizardcms/page/change_list.html"
    change_form_template = "admin/wizardcms/node/change_form.html"
    list_display = ('id','title','slug','language','get_navigation_path','status','created_at','updated_at')
    list_filter = ('language','parent','status','created_at','updated_at')
    list_select_related = True
    list_display_links= ('id','title','slug')
    # list_editable = ('title','slug','status')
    search_fields = ['id', 'title', 'slug']
    radio_fields = {
            'status': admin.HORIZONTAL,
            }
    tabs = {
      'common': {
          'title': _('Common'),
          'prepopulated_fields':  {'slug': ('title',)},
          'fieldsets': (
            (_('Node description'), {
                'classes': ('left',),
                'description': _(u'Provide page title, short title for menus and slug for friendly links.'),
                'fields': ['title', 'short_title', 'slug', 'content_type'],
                }),
            (_('Publication options'), {
                'description': _(u'Change publication settings here. Leave fields "publish from" and "publish to" empty for infinite publishing.'),
                'classes': ('right',),
                'fields': [('language','parent',),'status'],
                }),
            ),
          },
      'meta': {
          'title': _('Meta data'),
          'fieldsets': (
              (_('Meta data'), {
                  'fields': ['meta_description','meta_keywords','meta_author'],
                  }),
              )
          },
      }

    #    def _get_content_object_admin(self, object_id):
    #    node = models.Node.objects.get(pk=object_id)
    #    model_class = node.content_type.model_class()
    #    if model_class in self.admin_site._registry:
    #        admin_instance = self.admin_site._registry[model_class]
    #    return admin_instance


    def get_form(self, request, obj=None, **kwargs):
        if obj.content_type_id:
            if self.declared_fieldsets:
                fields = flatten_fieldsets(self.declared_fieldsets)
            else:
                fields = None
            if self.exclude is None:
                exclude = []
            else:
                exclude = list(self.exclude)
            model_class = obj.content_object or obj.content_type.model_class()
            defaults = {
                "form": self.form,
                "fields": fields,
                "exclude": exclude + kwargs.get("exclude", []),
                "formfield_callback": self.formfield_for_dbfield,
            }
            defaults.update(kwargs)
            return modelform_factory(model=model_class, 
                    **defaults)
        return super(NodeAdmin, self).get_form(self, request, obj, **kwargs)

#    def change_view(self, request, object_id, extra_context=None):
#        return self._get_content_object_admin(object_id).change_view(request, object_id, extra_context)

#    def delete_view(self, request, object_id, extra_context=None):
#        return self._get_content_object_admin(object_id).delete_view(request, object_id, extra_context)

#    def history_view(self, request, object_id, extra_context=None):
#        return self._get_content_object_admin(object_id).history_view(request, object_id, extra_context)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'symbol', 'name', 'description',)
    list_display_links = ('id', 'symbol', 'name',)
    search_fields = ('id', 'symbol', 'name', 'description',)

class PageAdmin(tabadmin.TabbedModelAdmin):
    change_list_template = "admin/wizardcms/page/change_list.html"
    list_display = ('id','title','slug','language','get_navigation_path','status','category','display_order','created_at','updated_at')
    list_filter = ('language','category','status','created_at','updated_at')
    list_select_related = True
    list_display_links= ('id','title','slug')
    # list_editable = ('title','slug','status')
    search_fields = ['id', 'title', 'slug']
    radio_fields = {
            'status': admin.HORIZONTAL,
            }
    inlines = [PageSectionInline]
    list_editable = ('display_order',)
    tabs_order = ['common','attachments','meta',]
    tabs = {
      'common': {
          'title': _('Common'),
          'prepopulated_fields':  {'slug': ('title',)},
          'fieldsets': (
            (_('Page description'), {
                'classes': ('left',),
                'description': _(u'Provide page title, short title for menus and slug for friendly links.'),
                'fields': ['title', 'short_title', 'introduction', 'description', 'photo',],
                }),
            (_('Publication options'), {
                'description': _(u'Change publication settings here. Leave fields "publish from" and "publish to" empty for infinite publishing.'),
                'classes': ('right',),
                'fields': [('language','parent','category',),'status',('publish_from','publish_to',),'slug',('template','post_date',),],
                }),
            ),
          'inlines': [PageSectionInline],
          },
      'attachments': {
          'title': _('Attachments'),
          'fieldsets': (),
          'inlines': [PageAttachmentInline],
          },
      'meta': {
          'title': _('Meta data'),
          'fieldsets': (
              (_('Meta data'), {
                  'fields': ['meta_description','meta_keywords','meta_author'],
                  }),
              )
          },
      'gallery': {
          'title': _('Gallery'),
          'fieldsets': (),
          }
      }

    class Media:
        css = {
                'all': (settings.ADMIN_MEDIA_PREFIX+'wizardcms/css/page.css',),
            }

    def queryset(self, request):
        parent_id = request.GET.get('parent__id__exact', None)
        qs = super(PageAdmin, self).queryset(request)
        if parent_id:
            qs = qs.filter(parent=parent_id)
        return qs


class Tree(object):
    def __init__(self, nodes=None):
        self.nodes = nodes or []


class TreeNode(object):
    def __init__(self, value, parent=None, children=None, url=None):
        self.children = children or []
        self.parent = parent
        self.value = value
        self.url = url

#    def __getattr__(self, key):
#        return self.value.__getattr__(key)

    def __unicode__(self):
        return unicode(self.value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "[TreeNode: %s (child of %s), children count: %d]" % (str(self), repr(self.parent), len(self.children))


class NodeTreeNavigation(object):
    def __init__(self, current_node, url_template):
        self.current = current_node 
        self.url_template = url_template
        self._tree = None

    @property
    def tree(self):
        return self._tree or self._build_tree()

    def _fill_node(self, basenode):
        children = basenode.value.child_nodes.all()

        if children.count():
            basenode.url = "?parent__id__exact=%s" % str(basenode.value.id)
        else:
            basenode.url = "../page/%d/" % basenode.value.id

        for node in children:
            if node.has_children():
                tnode = TreeNode(node, basenode)
                self._fill_node(tnode)
                basenode.children.append(tnode)

    def _build_tree(self):
        tree = Tree()

        for node in models.Node.objects.roots():
            if node.has_children():
                tnode = TreeNode(node)
                self._fill_node(tnode)
                tree.nodes.append(tnode)

        self._tree = tree
        return tree

    def get_url(self, node):
        return "/wizardcms/page/?parent__id__exact=%d" % node.id


site.register(models.Page, PageAdmin)
#site.register(models.Node, NodeAdmin)
site.register(models.Category, CategoryAdmin)
site.register(models.Menu, MenuAdmin)
site.register(models.Language)
site.register(models.Template, TemplateAdmin)

try:
    from antymedia.antyadmin import sitemenu
    from plugins import CmsSummary
    from django.conf import settings
    sitemenu.connect('apps', _('Content management'), settings.ADMIN_URL + 'wizardcms', name='apps.wizardcms')
    sitemenu.connect('apps', _('Announcements'), settings.ADMIN_URL + 'announcements')
    sitemenu.connect('apps', _('Text blocks'), settings.ADMIN_URL + 'chunks')
    site.register_dashboard(CmsSummary())
except ImportError, e:
    print e
    pass
