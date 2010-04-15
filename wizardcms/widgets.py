from django_widgets import Widget as BaseWidget
import models
from django import forms
from django.template.loader import get_template_from_string, Context, render_to_string
from django.template import TemplateSyntaxError, TemplateDoesNotExist, compile_string
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _



class Widget(BaseWidget):
    def get_context(self, value, options):
        return options or {}


class Menu(Widget):
    template = 'wizardcms/widgets/menu.html'
    
    class Media:
        css = {'all': ( 'widgets/css/menu.css' ),}

    def get_context(self, value, options):
        try:
            return {
                'menu': models.Menu.objects.published().get(symbol=value),
                }
        except models.Menu.DoesNotExist:
            return {}
        

class WizardCmsRenderPage(Widget):
    template = 'wizardcms/pages/page_content.html'

    def get_context(self, page, options):
        return {'page': page,}

class AdminTemplateEditWidget(forms.widgets.Textarea):
    def render(self, name, value, attrs=None):
        result = []
        value = value or ""
        result.append(super(AdminTemplateEditWidget, self).render(name, value, attrs))

        try:
            compile_string(value, None)
            result.append(u'<p class="template ok">%s</p>' % _('Template syntax is valid'))
        except (TemplateSyntaxError, TemplateDoesNotExist), e:
            msg = _('Template has following errors:')
            error = e
            if isinstance(e, TemplateDoesNotExist):
                error = _('Template does not exist: %s') % e
            result.append('<p class="template error"><span>%s</span> %s</p>' % (msg, error))
        return mark_safe(u''.join(result))
            

class GlobalSearch(Widget):
    def render(self, name, session, attrs=None):
        ctx = {
               'keyword': session.get('wizardcms.search.keyword') or '',
               }
        return render_to_string('wizardcms/widgets/global_search.html', ctx)


class AdminCategoryTreeWidget(forms.widgets.Select):
    pass
