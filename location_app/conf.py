from django.conf import settings as django_settings
from django.core.exceptions import ImproperlyConfigured


class AppSettings(object):
    prefix = 'LOC_APP'
    required_settings = ['MAPS_API_KEY']

    defaults = {
        'MAPS_API_KEY': None,
        # 'MAP_AUTOCOMPLETE_OPTIONS': '{"type": "establishment"}',
        # 'MAP_SIZE': "20rem",
        'MAP_OPTIONS': '{"center": {"lat": 40.7127753, "lng": -74.0059728}, "zoom": 16, "scale": 2, "draggable": false}',
        'MARKER_OPTIONS': '{"draggable": false}',
    }

    def __init__(self, django_settings):
        self.django_settings = django_settings

        for setting in self.required_settings:
            prefixed_name = '%s_%s' % (self.prefix, setting)
            if not hasattr(self.django_settings, prefixed_name):
                raise ImproperlyConfigured(
                    "The '%s' setting is required." % prefixed_name
                )

    def __getattr__(self, name):
        prefixed_name = '%s_%s' % (self.prefix, name)
        
        if hasattr(django_settings, prefixed_name):
            return getattr(django_settings, prefixed_name)

        if name in self.defaults:
            return self.defaults[name]
        
        raise AttributeError(
            "'AppSettings' object does not have a '%s' attribute" % name
        )


settings = AppSettings(django_settings)