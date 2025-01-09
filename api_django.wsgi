import os, sys

# Caminho para o activate_this.py do virtualenv
activate_this = '/home/ncdd/apps_wsgi/api_django/env_django/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Ajuste os caminhos para o projeto
sys.path.append('/home/ncdd/apps_wsgi')
sys.path.append('/home/ncdd/apps_wsgi/api_django')

os.environ['PYTHON_EGG_CACHE'] = '/home/ncdd/apps_wsgi/.python-eggs'
os.environ['DJANGO_SETTINGS_MODULE'] = 'api_django.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()