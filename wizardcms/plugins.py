"""
WizardCMS plugins API
"""

from django import template 
from wizardcms import models 


"""
Dashboard
"""

try:

    class CmsSummary(object):
        title = "Podsumowanie CMS"
        def render(self):
            data = {
                    'pages': {
                        'published': models.Page.objects.all().published().count(),
                        'overall':  models.Page.objects.all().count(),
                        'in_work': models.Page.objects.all().in_work().count(),
                        'proof_reading': models.Page.objects.all().in_proof_reading().count(),
                        'accepted': models.Page.objects.all().accepted().count(),
                        'new': models.Page.objects.all().new().count(),
                        'assigned': models.Page.objects.all().assigned().count(),
                        },
                    }
            return template.loader.render_to_string(
                    'wizardcms/dashboard/summary.html', 
                    data)
            
except ImportError:
    pass

