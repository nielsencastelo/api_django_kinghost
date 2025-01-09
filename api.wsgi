import sys

activate_this = '/home/ncdd/apps_wsgi/api/env/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Observe a barra inicial no caminho
sys.path.append('/home/ncdd/apps_wsgi/api')

from run import app as application
