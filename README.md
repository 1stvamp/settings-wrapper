[django_project/settings.py](./django_project/settings.py) is a regular Python module,
as you might use for your Django settings module.

The magic happens in [patch_settings.py](./patch_settings.py) which replaces the settings
with a wrapper object in which we have a dynamic attribute `STATIC_URL` which
can change based on different conditions.
