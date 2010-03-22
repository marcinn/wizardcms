from django.contrib.admin import site
from django.shortcuts import render_to_response
from django import template
import sitemenu

class AntyAdmin:
    def dashboard(self, request, extra_context=None):
        context = {
                'dashboard': self.dashboards if hasattr(self,'dashboards') else (),
                }
        return render_to_response('antyadmin/dashboard.html', context, 
                context_instance = template.RequestContext(request))

    def register_dashboard(self, dashboard):
        if not hasattr(self, 'dashboards'):
            self.dashboards = []
        self.dashboards.append(dashboard)

    def unregister_dashboard(self, dashboard):
        if not hasattr(self, 'dashboards'):
            self.dashboards = []
        for i, d in enumerate(self.dashboards):
            if isinstance(d, dashboard):
                self.dashboards.pop(i)

    def connect_menu(self, *args, **kwargs):
        return sitemenu.connect(*args, **kwargs)

    def disconnect_menu(self, *args, **kwargs):
        return sitemenu.disconnect(*args, **kwargs)

    def index(self, request, extra_context=None):
        return self.dashboard(request, extra_context)

"""
create mixin for original django admin site
"""

from admin import site
site.__class__.__bases__ = (AntyAdmin, ) + site.__class__.__bases__
site.index = site.dashboard


from antymedia.antyadmin import sitemenu as menu
 
menu.connect('root', 'Moduly', pri=20, name='apps')
menu.connect('root', 'Narzedia', pri=15, name='tools')
menu.connect('root', 'Ustawienia', pri=10, name='settings')

site.menu_connect = menu.connect

