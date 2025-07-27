<<<<<<< HEAD
"""
WSGI config for newyear project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newyear.settings')

application = get_wsgi_application()

app = application
=======
"""
WSGI config for newyear project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newyear.settings')

application = get_wsgi_application()
>>>>>>> f3a8a26eb894af3d5e70e5dde272d241869820c7
