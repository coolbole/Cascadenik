""" cascadnik - cascading sheets of style for mapnik

http://mike.teczno.com/notes/cascadenik.html

http://code.google.com/p/mapnik-utils/wiki/Cascadenik

"""
from os import mkdir, chmod
from os.path import isdir, realpath, expanduser, dirname, exists
from urlparse import urlparse

import style
# compile module
import compile as _compile
# compile function
from compile import compile, Directories
from style import stylesheet_declarations

# define Cascadenik version
VERSION = '0.2.0'
CACHE_DIR = '~/.cascadenik'

__all__ = ['load_map', 'compile','_compile','style','stylesheet_declarations']

def load_map(map, input, target_dir, cache_dir=None, datasources_cfg=None, verbose=False):
    """
    """
    scheme, n, path, p, q, f = urlparse(input)
    
    if scheme in ('file', ''):
        assert exists(input), "We'd prefer an input file that exists to one that doesn't"
    
    if cache_dir is None:
        cache_dir = expanduser(CACHE_DIR)
        
        # only make the cache dir if it wasn't user-provided
        if not isdir(cache_dir):
            mkdir(cache_dir)
            chmod(cache_dir, 0755)

    dirs = Directories(target_dir, realpath(cache_dir), dirname(input))
    compile(input, dirs, verbose, datasources_cfg=datasources_cfg).to_mapnik(map, dirs)
