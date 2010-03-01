from netwizard.wizardcms import models
from django.conf import settings

__all__ = ['pages', 'menus']


class BaseFront(object):
    def _page_as_dict(self, page):
        intro = page.sections.all()[0].content \
                if page.sections.all().count() \
                else None
        return {
                'id': page.id,
                'title': page.title,
                'short_title': page.short_title or page.title,
                'updagted_at': page.updated_at,
                'introduction': intro,
                'sections': [self._section_as_dict(d) for d in page.sections.all()],
            }

    def _section_as_dict(self, s):
        return {
                'title': s.title,
                'content': s.content
            }
        
    def _menu_as_dict(self, m):
        return {
            'id': m.id,
            'symbol': m.symbol,
            'name': m.name,
            'items': [{'id':n.id, 'short_title': n.title, 'title':n.title, 'url': n.url} for n in m.items.published()],
        }


class FrontPages(BaseFront):

    def get_pages(self, category=None, limit=10, offset=0):
        l = models.Page.objects.published().select_related().all()
        if category: 
            l.filter(parent=category)
        return [self._page_as_dict(p) for p in l[offset:limit]]

    def get_page(self, id):
        page = models.Page.objects.published().select_related().get(id=id)
        return page
        #return self._page_as_dict(page)

    def get_page_metas(self, id):
        page = models.Page.objects.published().select_related().get(id=id)
        return {
                'keywords': page.meta_keywords,
                'description': page.meta_description,
            }

    def get_page_list_metas(self, category_id):
       return {}
   

class FrontMenus(BaseFront):
    def get(self, id=None, symbol=None):
        try:
            if symbol:
                return self._menu_as_dict(models.Menu.objects.published().get(symbol=symbol))
            if id:
                return self._menu_as_dict(models.Menu.objects.published().get(id=id))
        except models.Menu.DoesNotExist, e:
            pass
        return {}
    

pages = FrontPages()
menus = FrontMenus()
