from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import *
from .conf import settings
from .widgets import LocationAppWidget


class LocationForm(forms.Form):
	"""
	ToDo: Make it such that location should be selected from dropdown otherwise show an error
	"""
	location = forms.CharField(required=False,label="Enter Location", help_text="Enter the location.")
	location.widget = LocationAppWidget()

	place = forms.CharField(label="Place")
	place_id = forms.CharField(label="Place Id")
	longitude = forms.FloatField(label="Longitude")
	latitude = forms.FloatField(label="Latitude")
	city = forms.CharField(required=False, label="City")
	state = forms.CharField(required=False, label="State")
	country = forms.CharField(label="Country")


	def save(self):
		plc_id = self.cleaned_data.get('place_id', None)
		if plc_id is not None:
			try:
				place_instance = Place.objects.get(place_id=plc_id)
			except:
				place_instance = None

			if place_instance is None:

				country_val = self.cleaned_data.get('country', None)
				if country_val is not None:
					try:
						country_instance = Country.objects.get(name=country_val)
					except Exception as e:
						country_instance = Country(name=country_val)
						country_instance.save()
				else:
					#we were expecting country value to be received, something went wrong
					raise ValidationError("country value was not received")


				state_val = self.cleaned_data.get('state', None)
				state_instance = None
				if state_val is not None:
					try:
						state_instance = AdministrativeArea.objects.get(name=state_val)
					except Exception as e:
						state_instance = AdministrativeArea(name=state_val, country=country_instance)
						state_instance.save()


				city_val = self.cleaned_data.get('city', None)
				city_instance = None
				if city_val is not None:
					try:
						city_instance = Locality.objects.get(name=city_val)
					except Exception as e:
						city_instance = Locality(name=city_val, state=state_instance, country=country_instance)
						city_instance.save()

				try:
					place_instance = Place(name=self.cleaned_data['place'],
						                   place_id=self.cleaned_data['place_id'],
		                                   longitude=self.cleaned_data['longitude'],
		                                   latitude=self.cleaned_data['latitude'],
		                                   city = city_instance,
		                                   state = state_instance,
		                                   country = country_instance,
		                                   )
					place_instance.save()
				except Exception as e:
					raise ValueError(repr(e))

			return place_instance

		else:
			raise ValidationError("place_id is a required field and was missing in the input")