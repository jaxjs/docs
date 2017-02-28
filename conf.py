import sys, os
from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer

sys.path.append(os.path.abspath('_exts'))

extensions = []
master_doc = 'index'
highlight_language = 'javascript'

project = u'Jax JavaScript HTTP Library'
copyright = u'2017 Nick Sagona, III'

version = '5'
release = '5.5.0'

