import os
import sys

sys.path.append('/opt/')
sys.path.append('/opt/helios')
sys.path.append('/opt/helios/venv/lib/python3.10/site-packages')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
