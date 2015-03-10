import django_project
from django_project import settings
from types import ModuleType
from random import choice


keys = ('foo', 'bar', 'baz')


class module(ModuleType):
    def __getattr__(self, name):
        if name == 'STATIC_URL':
            return settings.STATIC_URL_MAP[choice(keys)]
        return getattr(settings, name)

    def __setattr__(self, name, value):
        return setattr(settings, name, value)

    def __dir__(self):
        d = dir(settings)
        d.append('STATIC_URL')
        return d


django_project.settings = module('django_project.settings')
