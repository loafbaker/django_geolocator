from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from .functions import locu_search, foursquare_search


def home(request):
	context = {}
	context.update(csrf(request))

	if request.method == 'POST':
		print request.POST
		query = request.POST['search']

		# Option 1: Locu Search
		# locations = locu_search(query)
		# Option 2: Foursquare Search
		locations = foursquare_search(query)

		context['query'] = query
		context['locations'] = locations

	return render_to_response('home.html', context)