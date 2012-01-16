import jinja2


from firmant.settings import *


CONTENT_ROOT    = '.'
TEMPLATE_LOADER = jinja2.ChoiceLoader([
    jinja2.FileSystemLoader('templates')
   ,jinja2.PackageLoader('firmant', 'templates')
])
