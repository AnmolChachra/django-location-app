from django import forms
from django.utils.translation import ugettext_lazy as _

from .conf import settings

class LocationAppWidget(forms.widgets.TextInput):
	def __init__(self, attrs=None):
		super(LocationAppWidget, self).__init__(attrs)

	class Media:
		js = ('//maps.googleapis.com/maps/api/js?key={}&libraries=places'.format(settings.MAPS_API_KEY),
        	 )
