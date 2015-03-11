import django_project
from django_project import settings
from threading import local
from types import ModuleType


class module(ModuleType):
    def __getattr__(self, name):
        if name == 'STATIC_URL':
            d = local()
            request = d.django_current_request
            return settings.STATIC_URL_MAP[request.META.get('HTTP_HOST')]
        return getattr(settings, name)

    def __setattr__(self, name, value):
        return setattr(settings, name, value)

    def __dir__(self):
        d = dir(settings)
        d.append('STATIC_URL')
        return d


django_project.settings = module('django_project.settings')
