import sys, os

def initialize_sys_path():
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    dirs = (
            'django-announcements', 
            'django-attachments', 
            os.path.join('django-markup','src'),
            'django-positions', 
            'django-wysiwyg',
            #'django-flatblocks',
            'django-chunks',
            )
         
    for dir in dirs:
        sys.path.append(os.path.join(CURRENT_DIR, dir))

