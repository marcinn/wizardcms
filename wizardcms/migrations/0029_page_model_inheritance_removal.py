
from south.db import db
from django.db import models
from wizardcms.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'NewPage'
        db.create_table('wizardcms_newpage', (
            ('id', orm['wizardcms.newpage:id']),
            ('node', orm['wizardcms.newpage:node']),
            ('publish_from', orm['wizardcms.newpage:publish_from']),
            ('publish_to', orm['wizardcms.newpage:publish_to']),
            ('template', orm['wizardcms.newpage:template']),
            ('introduction', orm['wizardcms.newpage:introduction']),
            ('description', orm['wizardcms.newpage:description']),
            ('post_date', orm['wizardcms.newpage:post_date']),
            ('category', orm['wizardcms.newpage:category']),
            ('photo', orm['wizardcms.newpage:photo']),
        ))
        db.send_create_signal('wizardcms', ['NewPage'])
        
        # Changing field 'Node.level'
        # (to signature: django.db.models.fields.PositiveIntegerField(null=True, db_index=True))
        db.alter_column('wizardcms_node', 'level', orm['wizardcms.node:level'])
        
        # Changing field 'Node.tree_id'
        # (to signature: django.db.models.fields.PositiveIntegerField(null=True, db_index=True))
        db.alter_column('wizardcms_node', 'tree_id', orm['wizardcms.node:tree_id'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'NewPage'
        db.delete_table('wizardcms_newpage')
        
        # Changing field 'Node.level'
        # (to signature: django.db.models.fields.PositiveIntegerField(null=True, db_index=True))
        db.alter_column('wizardcms_node', 'level', orm['wizardcms.node:level'])
        
        # Changing field 'Node.tree_id'
        # (to signature: django.db.models.fields.PositiveIntegerField(null=True, db_index=True))
        db.alter_column('wizardcms_node', 'tree_id', orm['wizardcms.node:tree_id'])
        
    
    
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
        'wizardcms.link': {
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['wizardcms.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
        'wizardcms.newpage': {
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'new_pages'", 'null': 'True', 'to': "orm['wizardcms.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introduction': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wizardcms.Node']"}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'post_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'publish_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'publish_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wizardcms.Template']", 'null': 'True', 'blank': 'True'})
        },
        'wizardcms.node': {
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'display_order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wizardcms.Language']"}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'db_index': 'True'}),
            'meta_author': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'max_length': '160', 'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_nodes'", 'null': 'True', 'to': "orm['wizardcms.Node']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'db_index': 'True'}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'db_index': 'True'}),
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
