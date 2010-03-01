
from south.db import db
from django.db import models
from netwizard.wizardcms.models import *

class Migration:
    
    def forwards(self, orm):
        db.add_column('wizardcms_page', 'template', models.ForeignKey(Template, null=True))
    
    def backwards(self, orm):
        db.delete_column('wizardcms_page')
    
