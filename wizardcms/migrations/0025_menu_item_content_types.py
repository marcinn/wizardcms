
from south.db import db
from django.db import models
from wizardcms.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'MenuItem.content_type'
        db.add_column('wizardcms_menuitem', 'content_type', orm['wizardcms.menuitem:content_type'])
        
        # Adding field 'MenuItem.content_id'
        db.add_column('wizardcms_menuitem', 'content_id', orm['wizardcms.menuitem:content_id'])
        
        # Changing field 'PageAttachment.name'
        # (to signature: django.db.models.fields.CharField(max_length=255, null=True, blank=True))
        db.alter_column('wizardcms_pageattachment', 'name', orm['wizardcms.pageattachment:name'])
        
        # Changing field 'PageAttachment.file_path'
        # (to signature: django.db.models.fields.files.FileField(max_length=255))
        db.alter_column('wizardcms_pageattachment', 'file_path', orm['wizardcms.pageattachment:file_path'])
        
        # Changing field 'PageAttachment.is_published'
        # (to signature: django.db.models.fields.BooleanField(blank=True))
        db.alter_column('wizardcms_pageattachment', 'is_published', orm['wizardcms.pageattachment:is_published'])
        
        # Changing field 'Page.category'
        # (to signature: django.db.models.fields.related.ForeignKey(blank=True, null=True, to=orm['wizardcms.Category']))
        db.alter_column('wizardcms_page', 'category_id', orm['wizardcms.page:category'])
        
        # Changing field 'Page.publish_from'
        # (to signature: django.db.models.fields.DateField(null=True, blank=True))
        db.alter_column('wizardcms_page', 'publish_from', orm['wizardcms.page:publish_from'])
        
        # Changing field 'Page.description'
        # (to signature: django.db.models.fields.TextField(null=True, blank=True))
        db.alter_column('wizardcms_page', 'description', orm['wizardcms.page:description'])
        
        # Changing field 'Page.introduction'
        # (to signature: django.db.models.fields.TextField(null=True, blank=True))
        db.alter_column('wizardcms_page', 'introduction', orm['wizardcms.page:introduction'])
        
        # Changing field 'Page.photo'
        # (to signature: django.db.models.fields.files.ImageField(max_length=255, null=True, blank=True))
        db.alter_column('wizardcms_page', 'photo', orm['wizardcms.page:photo'])
        
        # Changing field 'Page.publish_to'
        # (to signature: django.db.models.fields.DateField(null=True, blank=True))
        db.alter_column('wizardcms_page', 'publish_to', orm['wizardcms.page:publish_to'])
        
        # Changing field 'Page.post_date'
        # (to signature: django.db.models.fields.DateField(null=True))
        db.alter_column('wizardcms_page', 'post_date', orm['wizardcms.page:post_date'])
        
        # Changing field 'Page.template'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['wizardcms.Template'], null=True, blank=True))
        db.alter_column('wizardcms_page', 'template_id', orm['wizardcms.page:template'])
        
        # Changing field 'Page.node_ptr'
        # (to signature: django.db.models.fields.related.OneToOneField(to=orm['wizardcms.Node'], unique=True, primary_key=True))
        db.alter_column('wizardcms_page', 'node_ptr_id', orm['wizardcms.page:node_ptr'])
        
        # Changing field 'MenuItem.title'
        # (to signature: django.db.models.fields.CharField(max_length=255, blank=True))
        db.alter_column('wizardcms_menuitem', 'title', orm['wizardcms.menuitem:title'])
        
        # Changing field 'MenuItem.display_order'
        # (to signature: django.db.models.fields.PositiveIntegerField())
        db.alter_column('wizardcms_menuitem', 'display_order', orm['wizardcms.menuitem:display_order'])
        
        # Changing field 'MenuItem.value'
        # (to signature: django.db.models.fields.CharField(max_length=255))
        db.alter_column('wizardcms_menuitem', 'value', orm['wizardcms.menuitem:value'])
        
        # Changing field 'MenuItem.type'
        # (to signature: django.db.models.fields.CharField(max_length=32))
        db.alter_column('wizardcms_menuitem', 'type', orm['wizardcms.menuitem:type'])
        
        # Changing field 'MenuItem.is_published'
        # (to signature: django.db.models.fields.BooleanField(blank=True))
        db.alter_column('wizardcms_menuitem', 'is_published', orm['wizardcms.menuitem:is_published'])
        
        # Changing field 'Language.is_active'
        # (to signature: django.db.models.fields.BooleanField(blank=True))
        db.alter_column('wizardcms_language', 'is_active', orm['wizardcms.language:is_active'])
        
        # Changing field 'Language.name'
        # (to signature: django.db.models.fields.CharField(max_length=64))
        db.alter_column('wizardcms_language', 'name', orm['wizardcms.language:name'])
        
        # Changing field 'Menu.name'
        # (to signature: django.db.models.fields.CharField(max_length=64))
        db.alter_column('wizardcms_menu', 'name', orm['wizardcms.menu:name'])
        
        # Changing field 'Menu.language'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['wizardcms.Language']))
        db.alter_column('wizardcms_menu', 'language_id', orm['wizardcms.menu:language'])
        
        # Changing field 'Menu.is_published'
        # (to signature: django.db.models.fields.BooleanField(blank=True))
        db.alter_column('wizardcms_menu', 'is_published', orm['wizardcms.menu:is_published'])
        
        # Changing field 'Category.description'
        # (to signature: django.db.models.fields.CharField(max_length=255, null=True, blank=True))
        db.alter_column('wizardcms_category', 'description', orm['wizardcms.category:description'])
        
        # Changing field 'Category.name'
        # (to signature: django.db.models.fields.CharField(max_length=255))
        db.alter_column('wizardcms_category', 'name', orm['wizardcms.category:name'])
        
        # Changing field 'PageSection.image_path'
        # (to signature: django.db.models.fields.files.ImageField(max_length=255, null=True, blank=True))
        db.alter_column('wizardcms_pagesection', 'image_path', orm['wizardcms.pagesection:image_path'])
        
        # Changing field 'PageSection.title'
        # (to signature: django.db.models.fields.CharField(max_length=255, null=True, blank=True))
        db.alter_column('wizardcms_pagesection', 'title', orm['wizardcms.pagesection:title'])
        
        # Changing field 'PageSection.markup'
        # (to signature: django.db.models.fields.CharField(max_length=1))
        db.alter_column('wizardcms_pagesection', 'markup', orm['wizardcms.pagesection:markup'])
        
        # Changing field 'PageSection.content'
        # (to signature: django.db.models.fields.TextField(blank=True))
        db.alter_column('wizardcms_pagesection', 'content', orm['wizardcms.pagesection:content'])
        
        # Changing field 'PageSection.template'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['wizardcms.Template']))
        db.alter_column('wizardcms_pagesection', 'template_id', orm['wizardcms.pagesection:template'])
        
        # Changing field 'PageSection.display_order'
        # (to signature: django.db.models.fields.PositiveIntegerField(blank=True))
        db.alter_column('wizardcms_pagesection', 'display_order', orm['wizardcms.pagesection:display_order'])
        
        # Changing field 'Template.name'
        # (to signature: django.db.models.fields.CharField(max_length=64))
        db.alter_column('wizardcms_template', 'name', orm['wizardcms.template:name'])
        
        # Changing field 'Template.content'
        # (to signature: django.db.models.fields.TextField())
        db.alter_column('wizardcms_template', 'content', orm['wizardcms.template:content'])
        
        # Changing field 'Template.path'
        # (to signature: django.db.models.fields.CharField(max_length=255, null=True, blank=True))
        db.alter_column('wizardcms_template', 'path', orm['wizardcms.template:path'])
        
        # Changing field 'Node.meta_description'
        # (to signature: django.db.models.fields.TextField(max_length=160, null=True, blank=True))
        db.alter_column('wizardcms_node', 'meta_description', orm['wizardcms.node:meta_description'])
        
        # Changing field 'Node.meta_keywords'
        # (to signature: django.db.models.fields.TextField(max_length=255, null=True, blank=True))
        db.alter_column('wizardcms_node', 'meta_keywords', orm['wizardcms.node:meta_keywords'])
        
        # Changing field 'Node.language'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['wizardcms.Language']))
        db.alter_column('wizardcms_node', 'language_id', orm['wizardcms.node:language'])
        
        # Changing field 'Node.parent'
        # (to signature: django.db.models.fields.related.ForeignKey(blank=True, null=True, to=orm['wizardcms.Node']))
        db.alter_column('wizardcms_node', 'parent_id', orm['wizardcms.node:parent'])
        
        # Changing field 'Node.title'
        # (to signature: django.db.models.fields.CharField(max_length=255))
        db.alter_column('wizardcms_node', 'title', orm['wizardcms.node:title'])
        
        # Changing field 'Node.meta_author'
        # (to signature: django.db.models.fields.CharField(max_length=64, null=True, blank=True))
        db.alter_column('wizardcms_node', 'meta_author', orm['wizardcms.node:meta_author'])
        
        # Changing field 'Node.created_at'
        # (to signature: django.db.models.fields.DateField(auto_now_add=True, blank=True))
        db.alter_column('wizardcms_node', 'created_at', orm['wizardcms.node:created_at'])
        
        # Changing field 'Node.updated_at'
        # (to signature: django.db.models.fields.DateField(auto_now=True, auto_now_add=True, blank=True))
        db.alter_column('wizardcms_node', 'updated_at', orm['wizardcms.node:updated_at'])
        
        # Changing field 'Node.short_title'
        # (to signature: django.db.models.fields.CharField(max_length=64, null=True, blank=True))
        db.alter_column('wizardcms_node', 'short_title', orm['wizardcms.node:short_title'])
        
        # Changing field 'Node.slug'
        # (to signature: django.db.models.fields.SlugField(db_index=True, max_length=255, unique=True, null=True, blank=True))
        db.alter_column('wizardcms_node', 'slug', orm['wizardcms.node:slug'])
        
        # Creating unique_together for [node_ptr] on Page.
        db.create_unique('wizardcms_page', ['node_ptr_id'])
        
    
    
    def backwards(self, orm):
        
        # Deleting unique_together for [node_ptr] on Page.
        db.delete_unique('wizardcms_page', ['node_ptr_id'])
        
        # Deleting field 'MenuItem.content_type'
        db.delete_column('wizardcms_menuitem', 'content_type_id')
        
        # Deleting field 'MenuItem.content_id'
        db.delete_column('wizardcms_menuitem', 'content_id')
        
        # Changing field 'PageAttachment.name'
        # (to signature: models.CharField(null=True, max_length=255, blank=True))
        db.alter_column('wizardcms_pageattachment', 'name', orm['wizardcms.pageattachment:name'])
        
        # Changing field 'PageAttachment.file_path'
        # (to signature: models.FileField(max_length=255))
        db.alter_column('wizardcms_pageattachment', 'file_path', orm['wizardcms.pageattachment:file_path'])
        
        # Changing field 'PageAttachment.is_published'
        # (to signature: models.BooleanField())
        db.alter_column('wizardcms_pageattachment', 'is_published', orm['wizardcms.pageattachment:is_published'])
        
        # Changing field 'Page.category'
        # (to signature: models.ForeignKey(orm.Category, null=True, blank=True))
        db.alter_column('wizardcms_page', 'category_id', orm['wizardcms.page:category'])
        
        # Changing field 'Page.publish_from'
        # (to signature: models.DateField(null=True, blank=True))
        db.alter_column('wizardcms_page', 'publish_from', orm['wizardcms.page:publish_from'])
        
        # Changing field 'Page.description'
        # (to signature: models.TextField(null=True, blank=True))
        db.alter_column('wizardcms_page', 'description', orm['wizardcms.page:description'])
        
        # Changing field 'Page.introduction'
        # (to signature: models.TextField(null=True, blank=True))
        db.alter_column('wizardcms_page', 'introduction', orm['wizardcms.page:introduction'])
        
        # Changing field 'Page.photo'
        # (to signature: models.ImageField(null=True, max_length=255, blank=True))
        db.alter_column('wizardcms_page', 'photo', orm['wizardcms.page:photo'])
        
        # Changing field 'Page.publish_to'
        # (to signature: models.DateField(null=True, blank=True))
        db.alter_column('wizardcms_page', 'publish_to', orm['wizardcms.page:publish_to'])
        
        # Changing field 'Page.post_date'
        # (to signature: models.DateField(null=True))
        db.alter_column('wizardcms_page', 'post_date', orm['wizardcms.page:post_date'])
        
        # Changing field 'Page.template'
        # (to signature: models.ForeignKey(orm.Template, limit_choices_to={'type':PAGE_TEMPLATE}, null=True, blank=True))
        db.alter_column('wizardcms_page', 'template_id', orm['wizardcms.page:template'])
        
        # Changing field 'Page.node_ptr'
        # (to signature: models.OneToOneField(orm['wizardcms.Node']))
        db.alter_column('wizardcms_page', 'node_ptr_id', orm['wizardcms.page:node_ptr'])
        
        # Changing field 'MenuItem.title'
        # (to signature: models.CharField(max_length=255, blank=True))
        db.alter_column('wizardcms_menuitem', 'title', orm['wizardcms.menuitem:title'])
        
        # Changing field 'MenuItem.display_order'
        # (to signature: models.PositiveIntegerField())
        db.alter_column('wizardcms_menuitem', 'display_order', orm['wizardcms.menuitem:display_order'])
        
        # Changing field 'MenuItem.value'
        # (to signature: models.CharField(max_length=255))
        db.alter_column('wizardcms_menuitem', 'value', orm['wizardcms.menuitem:value'])
        
        # Changing field 'MenuItem.type'
        # (to signature: models.CharField(max_length=32))
        db.alter_column('wizardcms_menuitem', 'type', orm['wizardcms.menuitem:type'])
        
        # Changing field 'MenuItem.is_published'
        # (to signature: models.BooleanField())
        db.alter_column('wizardcms_menuitem', 'is_published', orm['wizardcms.menuitem:is_published'])
        
        # Changing field 'Language.is_active'
        # (to signature: models.BooleanField())
        db.alter_column('wizardcms_language', 'is_active', orm['wizardcms.language:is_active'])
        
        # Changing field 'Language.name'
        # (to signature: models.CharField(max_length=64))
        db.alter_column('wizardcms_language', 'name', orm['wizardcms.language:name'])
        
        # Changing field 'Menu.name'
        # (to signature: models.CharField(max_length=64))
        db.alter_column('wizardcms_menu', 'name', orm['wizardcms.menu:name'])
        
        # Changing field 'Menu.language'
        # (to signature: models.ForeignKey(orm.Language))
        db.alter_column('wizardcms_menu', 'language_id', orm['wizardcms.menu:language'])
        
        # Changing field 'Menu.is_published'
        # (to signature: models.BooleanField())
        db.alter_column('wizardcms_menu', 'is_published', orm['wizardcms.menu:is_published'])
        
        # Changing field 'Category.description'
        # (to signature: models.CharField(null=True, max_length=255, blank=True))
        db.alter_column('wizardcms_category', 'description', orm['wizardcms.category:description'])
        
        # Changing field 'Category.name'
        # (to signature: models.CharField(max_length=255))
        db.alter_column('wizardcms_category', 'name', orm['wizardcms.category:name'])
        
        # Changing field 'PageSection.image_path'
        # (to signature: models.ImageField(null=True, max_length=255, blank=True))
        db.alter_column('wizardcms_pagesection', 'image_path', orm['wizardcms.pagesection:image_path'])
        
        # Changing field 'PageSection.title'
        # (to signature: models.CharField(null=True, max_length=255, blank=True))
        db.alter_column('wizardcms_pagesection', 'title', orm['wizardcms.pagesection:title'])
        
        # Changing field 'PageSection.markup'
        # (to signature: models.CharField(max_length=1))
        db.alter_column('wizardcms_pagesection', 'markup', orm['wizardcms.pagesection:markup'])
        
        # Changing field 'PageSection.content'
        # (to signature: models.TextField(blank=True))
        db.alter_column('wizardcms_pagesection', 'content', orm['wizardcms.pagesection:content'])
        
        # Changing field 'PageSection.template'
        # (to signature: models.ForeignKey(orm.Template, limit_choices_to={'type':SECTION_TEMPLATE}))
        db.alter_column('wizardcms_pagesection', 'template_id', orm['wizardcms.pagesection:template'])
        
        # Changing field 'PageSection.display_order'
        # (to signature: models.PositiveIntegerField(blank=True))
        db.alter_column('wizardcms_pagesection', 'display_order', orm['wizardcms.pagesection:display_order'])
        
        # Changing field 'Template.name'
        # (to signature: models.CharField(max_length=64))
        db.alter_column('wizardcms_template', 'name', orm['wizardcms.template:name'])
        
        # Changing field 'Template.content'
        # (to signature: models.TextField())
        db.alter_column('wizardcms_template', 'content', orm['wizardcms.template:content'])
        
        # Changing field 'Template.path'
        # (to signature: models.CharField(null=True, max_length=255, blank=True))
        db.alter_column('wizardcms_template', 'path', orm['wizardcms.template:path'])
        
        # Changing field 'Node.meta_description'
        # (to signature: models.TextField(null=True, max_length=160, blank=True))
        db.alter_column('wizardcms_node', 'meta_description', orm['wizardcms.node:meta_description'])
        
        # Changing field 'Node.meta_keywords'
        # (to signature: models.TextField(null=True, max_length=255, blank=True))
        db.alter_column('wizardcms_node', 'meta_keywords', orm['wizardcms.node:meta_keywords'])
        
        # Changing field 'Node.language'
        # (to signature: models.ForeignKey(orm.Language))
        db.alter_column('wizardcms_node', 'language_id', orm['wizardcms.node:language'])
        
        # Changing field 'Node.parent'
        # (to signature: models.ForeignKey(orm.Node, null=True, blank=True))
        db.alter_column('wizardcms_node', 'parent_id', orm['wizardcms.node:parent'])
        
        # Changing field 'Node.title'
        # (to signature: models.CharField(max_length=255))
        db.alter_column('wizardcms_node', 'title', orm['wizardcms.node:title'])
        
        # Changing field 'Node.meta_author'
        # (to signature: models.CharField(null=True, max_length=64, blank=True))
        db.alter_column('wizardcms_node', 'meta_author', orm['wizardcms.node:meta_author'])
        
        # Changing field 'Node.created_at'
        # (to signature: models.DateField(auto_now_add=True))
        db.alter_column('wizardcms_node', 'created_at', orm['wizardcms.node:created_at'])
        
        # Changing field 'Node.updated_at'
        # (to signature: models.DateField(auto_now_add=True, auto_now=True))
        db.alter_column('wizardcms_node', 'updated_at', orm['wizardcms.node:updated_at'])
        
        # Changing field 'Node.short_title'
        # (to signature: models.CharField(null=True, max_length=64, blank=True))
        db.alter_column('wizardcms_node', 'short_title', orm['wizardcms.node:short_title'])
        
        # Changing field 'Node.slug'
        # (to signature: models.SlugField(max_length=255, unique=True, null=True, blank=True))
        db.alter_column('wizardcms_node', 'slug', orm['wizardcms.node:slug'])
        
    
    
    models = {
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'wizardcms.category': {
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'wizardcms.language': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'wizardcms.menu': {
            'Meta': {'unique_together': "(('symbol', 'language'),)"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wizardcms.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'wizardcms.menuitem': {
            'content_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'display_order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['wizardcms.Menu']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'wizardcms.node': {
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'display_order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wizardcms.Language']"}),
            'meta_author': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_nodes'", 'null': 'True', 'to': "orm['wizardcms.Node']"}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        'wizardcms.page': {
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pages'", 'null': 'True', 'to': "orm['wizardcms.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'introduction': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['wizardcms.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'post_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'publish_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'publish_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wizardcms.Template']", 'null': 'True', 'blank': 'True'})
        },
        'wizardcms.pageattachment': {
            'file_path': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'attachments'", 'to': "orm['wizardcms.Page']"})
        },
        'wizardcms.pagesection': {
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'display_order': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_path': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'markup': ('django.db.models.fields.CharField', [], {'default': "'W'", 'max_length': '1'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sections'", 'to': "orm['wizardcms.Page']"}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wizardcms.Template']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'wizardcms.template': {
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        }
    }
    
    complete_apps = ['wizardcms']
