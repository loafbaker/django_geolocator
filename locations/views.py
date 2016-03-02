from django.shortcuts import render, render_to_response
from django_geolocator.functions import locu_details, foursquare_details

from .models import Location

# Create your views here.
def single_location(request, id):
	context = {}
	try:
		location = Location.objects.get(locu_id=id)
		locu = True
		foursquare = False
	except Location.DoesNotExist:
		location = Location.objects.get(four_id=id)
		locu = False
		foursquare = True
	except:
		location = 'This location cannot be found.'
		locu = False
		foursquare = False

	context['location'] = location

	if locu:
		details = locu_details(location.locu_id)
		context['details'] = details
	elif foursquare:
		details = foursquare_details(location.four_id)
		context['details'] = details

	return render_to_response('locations/single.html', context)