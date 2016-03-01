from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from locations.models import Location

from .functions import locu_search, foursquare_search


def home(request):
	context = {}
	context.update(csrf(request))

	if request.method == 'POST':
		print request.POST
		query = request.POST['search']

		# Option 1: Locu Search
		locations = locu_search(query)
		for loc in locations:
			name, locu_id = loc[0], loc[1]
			new_location, created = Location.objects.get_or_create(name=name, locu_id=locu_id)
			if created:
				print "Created new id for %s with locu id of %s" % (name, locu_id)
		# Option 2: Foursquare Search
		# locations = foursquare_search(query)

		context['query'] = query
		context['locations'] = locations

	return render_to_response('home.html', context)