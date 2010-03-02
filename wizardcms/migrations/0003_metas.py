
from south.db import db
from django.db import models
from wizardcms.models import *

class Migration:
    
    def forwards(self):
        db.add_column('wizardcms_node', 'meta_description', models.CharField(max_length=160, null=True))
        db.add_column('wizardcms_node', 'meta_keywords', models.CharField(max_length=255, null=True))
        db.add_column('wizardcms_node', 'meta_author', models.CharField(max_length=64, null=True))
    
    def backwards(self):
        db.delete_column('wizardcms_node', 'meta_author');
        db.delete_column('wizardcms_node', 'meta_keywords');
        db.delete_column('wizardcms_node', 'meta_description');
