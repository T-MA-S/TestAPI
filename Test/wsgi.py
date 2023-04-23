"""
WSGI config for Test project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from .init_db import create_super_admin

create_super_admin()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Test.settings')

application = get_wsgi_application()
