
from south.db import db
from django.db import models
from wizardcms.models import *

class Migration:
    
    def forwards(self):
        db.alter_column('wizardcms_node', 'slug', models.SlugField(unique=True, max_length=255, blank=True, null=True))
    
    def backwards(self):
        db.delete_index('wizardcms_node', ['slug'])
