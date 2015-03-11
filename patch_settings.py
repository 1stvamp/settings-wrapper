import django_project
from django_project import settings
from threading import local
from types import ModuleType


class module(ModuleType):
    def __getattr__(self, name):
        if name == 'STATIC_URL':
            return self.get_static_url()

        return getattr(settings, name)

    def __setattr__(self, name, value):
        return setattr(settings, name, value)

    def get_static_url(self):
        d = local()
        request = getattr(d, 'django_current_request')

        static_url = settings.STATIC_URL
        if request and request.META.get('HTTP_HOST') in \
                settings.STATIC_URLSTATIC_URL_MAP:
            static_url = settings.STATIC_URL_MAP[request.META.get('HTTP_HOST')]

        return static_url


django_project.settings = module('django_project.settings')
