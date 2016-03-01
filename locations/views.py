from django.shortcuts import render, render_to_response

from .models import Location

# Create your views here.
def single_location(request, id):
	context = {}
	try:
		location = Location.objects.get(locu_id=id)
	except Location.DoesNotExist:
		location = Location.objects.get(locu_id=id)
	except:
		location = 'This location cannot be found.'

	context['location'] = location

	return render_to_response('locations/single.html', context)