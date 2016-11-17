import os

from whitenoise.django import DjangoWhiteNoise
from configurations.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cuiquer.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
