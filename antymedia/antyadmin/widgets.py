try:
    from django_widgets import Widget
except ImportError:
    from netwizard.widgets import Widget

from antymedia.antyadmin.sitemenu import manager
from antymedia.antyadmin.settings import globals

class Sitemenu(Widget):
    template = 'admin/sitemenu.html'
    def get_context(self, name, value=None, options=None):
        return {
                'menu': manager.root.childs,
                }


class AntyBranding(Widget):
    def render(self, name, value=None, options=None):
        return globals.get('project.name', 'Antyadmin')


