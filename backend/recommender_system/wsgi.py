"""
WSGI config for recommender_system project.

This module contains the WSGI application used by Django's runserver.
It should expose a module-level variable named `application`.

For more information on this file, see
https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recommender_system.settings')

application = get_wsgi_application()
