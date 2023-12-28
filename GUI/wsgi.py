"""
WSGI config for GUI project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from GUI.settings import BASE_DIR
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GUI.settings')
application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(BASE_DIR, "static"))


