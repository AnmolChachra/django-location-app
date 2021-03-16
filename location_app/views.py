from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from .conf import settings
from location_app.forms import LocationForm


def index(request):
	"""
	View for the 'LocationForm' form
	"""
	if request.method == "POST":
		form = LocationForm(request.POST)
		if form.is_valid():
			_ = form.save()
			if request.POST.get('next', None) != None:
				return redirect(request.POST['next'])

			return redirect(reverse('location'))
		else:
			messages.error(request, "Something went wrong! See the errors below or try to reload the page.")
	else:
		form = LocationForm()


	context = {
				'form': form,
				}

	context["map_options"] = settings.MAP_OPTIONS
	context["marker_options"] = settings.MARKER_OPTIONS
	# context["map_autocomplete_options"] = settings.MAP_AUTOCOMPLETE_OPTIONS
	return render(request, 'location_app/location.html', context)