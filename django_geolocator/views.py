from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from .functions import locu_search


def home(request):
	context = {}
	context.update(csrf(request))

	if request.method == 'POST':
		print request.POST
		query = request.POST['search']
		locations = locu_search(query)
		context['query'] = query
		context['locations'] = locations

	return render_to_response('home.html', context)