
from south.db import db
from django.db import models
from netwizard.wizardcms.models import *

class Migration:
    
    def forwards(self):
        
        # Model 'Language'
        db.create_table('wizardcms_language', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('name', models.CharField(max_length=64)),
            ('is_active', models.BooleanField(default=False)),
        ))
        # Model 'Template'
        db.create_table('wizardcms_template', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('type', models.IntegerField(choices=TEMPLATE_TYPES)),
            ('name', models.CharField(max_length=64)),
            ('content', models.TextField()),
        ))
        
        # Mock Models
        Language = db.mock_model(model_name='Language', db_table='wizardcms_language', db_tablespace='', pk_field_name='id', pk_field_type=models.AutoField, pk_field_args=[], pk_field_kwargs={})
        Node = db.mock_model(model_name='Node', db_table='wizardcms_node', db_tablespace='', pk_field_name='id', pk_field_type=models.AutoField, pk_field_args=[], pk_field_kwargs={})
        
        # Model 'Node'
        db.create_table('wizardcms_node', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('language', models.ForeignKey(Language)),
            ('parent', models.ForeignKey(Node, null=True, blank=True)),
            ('status', models.IntegerField(choices=NODE_STATUSES)),
            ('title', models.CharField(max_length=255)),
            ('short_title', models.CharField(max_length=64, null=True, blank=True)),
            ('slug', models.SlugField()),
            ('created_at', models.DateField(auto_now_add=True)),
            ('updated_at', models.DateField(auto_now_add=True, auto_now=True)),
        ))
        
        # Mock Models
        Node = db.mock_model(model_name='Node', db_table='wizardcms_node', db_tablespace='', pk_field_name='id', pk_field_type=models.AutoField, pk_field_args=[], pk_field_kwargs={})
        
        # Model 'Page'
        db.create_table('wizardcms_page', (
            ('node_ptr', models.OneToOneField(Node)),
            ('publish_from', models.DateField(null=True, blank=True)),
            ('publish_to', models.DateField(null=True, blank=True)),
        ))
        
        # Mock Models
        Node = db.mock_model(model_name='Node', db_table='wizardcms_node', db_tablespace='', pk_field_name='id', pk_field_type=models.AutoField, pk_field_args=[], pk_field_kwargs={})
        Page = db.mock_model(model_name='Page', db_table='wizardcms_page', db_tablespace='', pk_field_name='node_ptr', pk_field_type=models.OneToOneField, pk_field_args=[Node], pk_field_kwargs={})
        Template = db.mock_model(model_name='Template', db_table='wizardcms_template', db_tablespace='', pk_field_name='id', pk_field_type=models.AutoField, pk_field_args=[], pk_field_kwargs={})
        
        # Model 'PageSection'
        db.create_table('wizardcms_pagesection', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(Page)),
            ('title', models.CharField(max_length=255, null=True, blank=True)),
            ('content', models.TextField(blank=True)),
            ('image_path', models.ImageField( max_length=255, null=True, blank=True, upload_to=os.path.join('uploads','pages') )),
            ('template', models.ForeignKey(Template)),
        ))
        
        # Mock Models
        Node = db.mock_model(model_name='Node', db_table='wizardcms_node', db_tablespace='', pk_field_name='id', pk_field_type=models.AutoField, pk_field_args=[], pk_field_kwargs={})
        Page = db.mock_model(model_name='Page', db_table='wizardcms_page', db_tablespace='', pk_field_name='node_ptr', pk_field_type=models.OneToOneField, pk_field_args=[Node], pk_field_kwargs={})
        
        # Model 'PageAttachment'
        db.create_table('wizardcms_pageattachment', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(Page)),
            ('name', models.CharField(max_length=255, null=True, blank=True)),
            ('file_path', models.FileField( max_length=255, upload_to=os.path.join('uploads','attachments') )),
            ('is_published', models.BooleanField(default=False)),
        ))
        
        # Mock Models
        Language = db.mock_model(model_name='Language', db_table='wizardcms_language', db_tablespace='', pk_field_name='id', pk_field_type=models.AutoField, pk_field_args=[], pk_field_kwargs={})
        
        # Model 'Menu'
        db.create_table('wizardcms_menu', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('symbol', models.CharField(max_length=32)),
            ('language', models.ForeignKey(Language)),
            ('name', models.CharField(max_length=64)),
            ('is_published', models.BooleanField(default=False)),
        ))
        # Mock Models
        Menu = db.mock_model(model_name='Menu', db_table='wizardcms_menu', db_tablespace='', pk_field_name='id', pk_field_type=models.AutoField, pk_field_args=[], pk_field_kwargs={})
        Node = db.mock_model(model_name='Node', db_table='wizardcms_node', db_tablespace='', pk_field_name='id', pk_field_type=models.AutoField, pk_field_args=[], pk_field_kwargs={})
        
        # M2M field 'Menu.items'
        db.create_table('wizardcms_menu_items', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('menu', models.ForeignKey(Menu, null=False)),
            ('node', models.ForeignKey(Node, null=False))
        )) 
        db.create_index('wizardcms_menu', ['symbol','language_id'], unique=True, db_tablespace='')
        
        
        db.send_create_signal('wizardcms', ['Language','Template','Node','Page','PageSection','PageAttachment','Menu'])
    
    def backwards(self):
        db.delete_table('wizardcms_menu_items')
        db.delete_table('wizardcms_menu')
        db.delete_table('wizardcms_pageattachment')
        db.delete_table('wizardcms_pagesection')
        db.delete_table('wizardcms_page')
        db.delete_table('wizardcms_node')
        db.delete_table('wizardcms_template')
        db.delete_table('wizardcms_language')
        
