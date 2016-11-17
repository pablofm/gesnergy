import os

from whitenoise.django import DjangoWhiteNoise
from configurations.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gesnergy.settings")
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
