"""
ASGI config for apartmentbackend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from apartment_backend.realtimesms import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apartmentbackend.settings')

application = get_asgi_application()




application = ProtocolTypeRouter({
    'websocket': URLRouter(routing.websocket_urlpatterns),
})
