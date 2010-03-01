
from south.db import db
from django.db import models
from netwizard.wizardcms.models import *

class Migration:
    
    def forwards(self, orm):
        db.add_column('wizardcms_pagesection', 'display_order', models.PositiveIntegerField(null=True))
        """
        for page in orm.Page.objects.all():
            order = 1
            for section in page.sections.all():
                section.display_order = order
                section.save()
                order += 1
        """
                
    
    def backwards(self, orm):
        db.delete_column('wizardcms_pagesection', 'display_order')
    
    
    models = {
        'wizardcms.pageattachment': {
            'file_path': ('models.FileField', [], {'max_length': '255'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('models.BooleanField', [], {'default': 'False'}),
            'name': ('models.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'page': ('models.ForeignKey', ['Page'], {})
        },
        'wizardcms.page': {
            'Meta': {'_bases': ['netwizard.wizardcms.models.Node']},
            'node_ptr': ('models.OneToOneField', ["orm['wizardcms.Node']"], {}),
            'publish_from': ('models.DateField', [], {'null': 'True', 'blank': 'True'}),
            'publish_to': ('models.DateField', [], {'null': 'True', 'blank': 'True'}),
            'template': ('models.ForeignKey', ['Template'], {'limit_choices_to': "{'type':PAGE_TEMPLATE}", 'null': 'True', 'blank': 'True'})
        },
        'wizardcms.language': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('models.BooleanField', [], {'default': 'False'}),
            'name': ('models.CharField', [], {'max_length': '64'})
        },
        'wizardcms.menu': {
            'Meta': {'unique_together': "(('symbol','language'),)"},
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('models.BooleanField', [], {'default': 'False'}),
            'items': ('models.ManyToManyField', ['Node'], {'related_name': "'menus'"}),
            'language': ('models.ForeignKey', ['Language'], {}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'symbol': ('models.CharField', [], {'max_length': '32'})
        },
        'wizardcms.pagesection': {
            'content': ('models.TextField', [], {'blank': 'True'}),
            'display_order': ('models.PositiveIntegerField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image_path': ('models.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'page': ('models.ForeignKey', ['Page'], {'related_name': '"sections"'}),
            'template': ('models.ForeignKey', ['Template'], {'limit_choices_to': "{'type':SECTION_TEMPLATE}"}),
            'title': ('models.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'wizardcms.template': {
            'content': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '64'}),
            'type': ('models.IntegerField', [], {})
        },
        'wizardcms.node': {
            'created_at': ('models.DateField', [], {'auto_now_add': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'language': ('models.ForeignKey', ['Language'], {}),
            'meta_author': ('models.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'meta_description': ('models.TextField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('models.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parent': ('models.ForeignKey', ["'self'"], {'null': 'True', 'blank': 'True'}),
            'short_title': ('models.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'slug': ('models.SlugField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'status': ('models.IntegerField', [], {}),
            'title': ('models.CharField', [], {'max_length': '255'}),
            'updated_at': ('models.DateField', [], {'auto_now_add': 'True', 'auto_now': 'True'})
        }
    }
    
    complete_apps = ['wizardcms']
