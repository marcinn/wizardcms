import os, sys

__initialized__ = False

def setup_env():
    global __initialized__
    if __initialized__:
        return

    VENDOR_DIR = os.path.join(os.path.dirname(__file__),'..', 'vendor')
    APPS_DIR = os.path.join(os.path.dirname(__file__),'..', 'apps')
    for file in os.listdir(VENDOR_DIR):
        path = os.path.join(VENDOR_DIR, file)
        if os.path.isdir(path):
            sys.path.insert(0, path)

    for file in os.listdir(APPS_DIR):
        path = os.path.join(APPS_DIR, file)
        if os.path.isdir(path):
            if not os.path.exists(os.path.join(path, '__init__.py'))\
                    and os.path.exists(os.path.join(path, 'src')):
                sys.path.insert(0, os.path.join(path, 'src'))
            else:
                sys.path.insert(0, os.path.realpath(path))

    __initialized__ = True



