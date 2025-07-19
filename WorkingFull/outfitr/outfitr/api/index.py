# api/index.py
from django.core.asgi import get_asgi_application
from asgiref.wsgi import WsgiToAsgi

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "outfitr_project.settings")

application = WsgiToAsgi(get_asgi_application())
