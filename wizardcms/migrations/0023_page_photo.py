
from south.db import db
from django.db import models
from netwizard.wizardcms.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Page.photo'
        db.add_column('wizardcms_page', 'photo', models.ImageField(verbose_name=_('page photo'), max_length=255, null=True, blank=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Page.photo'
        db.delete_column('wizardcms_page', 'photo')
        
    
    
    models = {
        'wizardcms.pageattachment': {
            'file_path': ('models.FileField', [], {'verbose_name': "_('file path')", 'max_length': '255'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('models.BooleanField', [], {'default': 'False', 'verbose_name': "_('is published')"}),
            'name': ('models.CharField', [], {'verbose_name': "_('name')", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'page': ('models.ForeignKey', ['Page'], {'related_name': "'attachments'"})
        },
        'wizardcms.page': {
            'Meta': {'_bases': ['netwizard.wizardcms.models.Node']},
            'category': ('models.ForeignKey', ['Category'], {'related_name': "'pages'", 'null': 'True', 'verbose_name': "_('category')", 'blank': 'True'}),
            'introduction': ('models.TextField', [], {'null': 'True', 'verbose_name': "_('introduction')", 'blank': 'True'}),
            'node_ptr': ('models.OneToOneField', ["orm['wizardcms.Node']"], {}),
            'photo': ('models.ImageField', [], {'verbose_name': "_('page photo')", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'post_date': ('models.DateField', [], {'null': 'True', 'verbose_name': "_('post date')"}),
            'publish_from': ('models.DateField', [], {'null': 'True', 'verbose_name': "_('publish from')", 'blank': 'True'}),
            'publish_to': ('models.DateField', [], {'null': 'True', 'verbose_name': "_('publish to')", 'blank': 'True'}),
            'template': ('models.ForeignKey', ['Template'], {'limit_choices_to': "{'type':PAGE_TEMPLATE}", 'null': 'True', 'verbose_name': "_('template')", 'blank': 'True'})
        },
        'wizardcms.menuitem': {
            'display_order': ('models.PositiveIntegerField', [], {'verbose_name': "_('display order')"}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('models.BooleanField', [], {'default': 'False', 'verbose_name': "_('is published')"}),
            'menu': ('models.ForeignKey', ['Menu'], {'related_name': "'items'"}),
            'title': ('models.CharField', [], {'default': "''", 'max_length': '255', 'verbose_name': "_('title')", 'blank': 'True'}),
            'type': ('models.CharField', [], {'max_length': '32', 'verbose_name': "_('type')"}),
            'value': ('models.CharField', [], {'max_length': '255', 'verbose_name': "_('value')"})
        },
        'wizardcms.language': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('models.BooleanField', [], {'default': 'False', 'verbose_name': "_('is active')"}),
            'name': ('models.CharField', [], {'max_length': '64', 'verbose_name': "_('name')"})
        },
        'wizardcms.menu': {
            'Meta': {'unique_together': "(('symbol','language'),)"},
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('models.BooleanField', [], {'default': 'False', 'verbose_name': "_('is published')"}),
            'language': ('models.ForeignKey', ['Language'], {'verbose_name': "_('language')"}),
            'name': ('models.CharField', [], {'max_length': '64', 'verbose_name': "_('name')"}),
            'symbol': ('models.CharField', [], {'max_length': '32'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label','model'),)", 'db_table': "'django_content_type'"},
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'wizardcms.category': {
            'description': ('models.CharField', [], {'verbose_name': "_('description')", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '255', 'verbose_name': "_('name')"}),
            'symbol': ('models.CharField', [], {'max_length': '64'})
        },
        'wizardcms.pagesection': {
            'content': ('models.TextField', [], {'verbose_name': "_('content')", 'blank': 'True'}),
            'display_order': ('models.PositiveIntegerField', [], {'verbose_name': "_('display order')", 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image_path': ('models.ImageField', [], {'verbose_name': "_('image path')", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'markup': ('models.CharField', [], {'default': "'W'", 'max_length': '1', 'verbose_name': "_('text format')"}),
            'page': ('models.ForeignKey', ['Page'], {}),
            'template': ('models.ForeignKey', ['Template'], {'limit_choices_to': "{'type':SECTION_TEMPLATE}", 'verbose_name': "_('template')"}),
            'title': ('models.CharField', [], {'verbose_name': "_('title')", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'wizardcms.template': {
            'content': ('models.TextField', [], {'verbose_name': "_('content')"}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '64', 'verbose_name': "_('name')"}),
            'path': ('models.CharField', [], {'verbose_name': "_('path')", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'type': ('models.IntegerField', [], {})
        },
        'wizardcms.node': {
            'content_type': ('models.ForeignKey', ['ContentType'], {}),
            'created_at': ('models.DateField', [], {'auto_now_add': 'True', 'verbose_name': "_('created at')"}),
            'display_order': ('models.PositiveIntegerField', [], {'default': '0'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'language': ('models.ForeignKey', ['Language'], {'verbose_name': "_('language')"}),
            'meta_author': ('models.CharField', [], {'verbose_name': "_('meta author')", 'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'meta_description': ('models.TextField', [], {'verbose_name': "_('meta description')", 'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('models.TextField', [], {'verbose_name': "_('meta keywords')", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parent': ('models.ForeignKey', ["'self'"], {'related_name': '"child_nodes"', 'null': 'True', 'verbose_name': "_('parent node')", 'blank': 'True'}),
            'short_title': ('models.CharField', [], {'verbose_name': "_('short title')", 'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'slug': ('models.SlugField', [], {'null': 'True', 'max_length': '255', 'blank': 'True', 'unique': 'True', 'verbose_name': "_('slug')"}),
            'status': ('models.IntegerField', [], {}),
            'title': ('models.CharField', [], {'max_length': '255', 'verbose_name': "_('title')"}),
            'updated_at': ('models.DateField', [], {'auto_now_add': 'True', 'auto_now': 'True', 'verbose_name': "_('updated at')"})
        }
    }
    
    complete_apps = ['wizardcms']
