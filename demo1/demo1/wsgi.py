"""
WSGI config for demo1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo1.settings')

application = get_wsgi_application()

"""
Web 服务器会指定特定的WSGI 
WSGI指定Web应用入口函数
"""
