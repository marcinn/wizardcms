"""
sitemenu module
"""

import heapq
import exceptions

class MenuError(exceptions.BaseException):
    """
    base sitemenu exception
    """
    pass

class DuplicateMenuKeyError(MenuError):
    """
    error raised when named menu item is duplicated
    """
    pass

class NodeDoesNotExist(MenuError):
    """
    raised when accessing non-existent named node
    """
    pass

class Node(object):
    """
    represents node
    """
    def __init__(self, value):
        """
        creates node with value 
        value can be of any type
        """
        self.value = value
        self._childs = []
        self.parent = None

    @property
    def has_childs(self):
        return len(self._childs) >0

    @property
    def childs(self):
        """
        returns node childs in valid order
        """
        nodes = [node for pri, node in self._childs]
        nodes.reverse()
        return nodes

    def add_child(self, node, pri=0):
        """
        adds child Node with specified priority (default 0)
        """
        heapq.heappush(self._childs, (pri, node))

    def remove_child(self, node):
        for i, (pri, child) in enumerate(self._childs):
            if child == node:
                self._childs.pop(i)


    def __repr__(self):
        """
        representation of Node
        """
        return '[%s "%s" (%d childs)]' % (self.__class__.__name__, 
                self.value, len(self._childs))
    
    
class MenuNode(Node):
    """
    extended Node for handling menu nodes
    menu nodes have caption and url properties
    """
    
    def __init__(self, caption, url=None):
        """
        initialize node with caption and url
        """
        super(MenuNode, self).__init__((caption, url))
    
    @property
    def caption(self):
        """
        returns node caption
        """
        return self.value[0]
    
    @property
    def url(self):
        """
        returns node url
        """
        return self.value[1]
    

class MenuManager(object):
    """
    manager handles menu nodes
    """
    def __init__(self):
        """
        initializes root item
        """
        self.items = {
            'root': Node('root'),
          }
        
    def connect(self, node, key=None, parent=None, pri=0):
        """
        connects node instance to manager to 'root' (default) or parent
        key argument is used for naming nodes (must be unique)
        """
        if key:
            if self.items.has_key(key):
                raise DuplicateMenuKeyError(
                        'Node "%s" already registered' % key)
            self.items[key] = node
            
        parent = parent or 'root'
        if not self.items.has_key(parent):
            raise NodeDoesNotExist('Node "%s" does not exists' % parent)
        node.parent = self.items[parent]
        node.parent.add_child(node, pri)

    def disconnect(self, name):
        if self.items.has_key(name):
            node = self.items.pop(name)
            node.parent.remove_child(node)
        
    @property
    def root(self):
        """
        returns root node
        """
        return self.items['root']
    
    def __getitem__(self, key):
        """
        easy access to named nodes
        """
        return self.items[key].childs
    

# apps-wide manager instance
manager = MenuManager()
    
def connect(to, caption, url=None, pri=0, name=None):
    """
    helper for easy creating and connecting
    menu nodes to apps-wide manager
    """
    # workaround for django double-imports (ie. with south commands)
    return try_connect(to, caption, url, pri, name) 
    manager.connect(MenuNode(caption, url), pri=pri, parent=to, key=name)

def disconnect(name):
    manager.disconnect(name)

def try_connect(to, caption, url=None, pri=0, name=None):
    """
    helper for easy creating and connecting
    menu nodes to apps-wide manager
    if menu already exists function silently ends
    """
    try:
        manager.connect(MenuNode(caption, url), pri=pri, parent=to, key=name)
    except DuplicateMenuKeyError:
        pass


# unit test ;)

if __name__ == '__main__':

    menu = manager
    menu.connect(Node('Applications'), 'apps')
    menu.connect(Node('WizardCMS'), 'apps.wizardcms', 'apps')
    menu.connect(MenuNode('WebOffer', 'http://weboffer.pl'),
            'apps.weboffer', 'apps', 100)
    
    connect('apps', 'Photo gallery', 'http://photogallery.pl', pri=40)
    connect('apps', 'Datasource manager', 'http://datasourcemgr', 
            pri=60, name='apps.datasourcemanager')
    
    print menu['root']
    print menu['apps']
    

    disconnect('apps.datasourcemanager')
    print menu['apps']

