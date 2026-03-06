"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
<<<<<<< HEAD:Django/mysite/mysite/wsgi.py
=======


>>>>>>> 94a8095e87922dd792149161c5afb3a40cc2ee10:Django/mysite/wsgi.py
