import sys, os
from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer

sys.path.append(os.path.abspath('_exts'))

extensions = []
master_doc = 'index'
highlight_language = 'javascript'

project = u'Jax JavaScript Library'
copyright = u'2016 Nick Sagona, III'

version = '4'
release = '4.0.0'

lexers['javascript'] = JavaScriptLexer(startinline=True)

