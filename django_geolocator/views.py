from django.shortcuts import render

from locations.models import Location

from .functions import locu_search, foursquare_search, find_city_lat_lng


def home(request):
	context = {}

	if request.method == 'POST':
		# print(request.POST)
		query = request.POST['search']

		try:
			lat = request.POST['lat']
			lng = request.POST['lng']
			local_query = find_city_lat_lng(lat, lng)
			if query == '':
				query = local_query
		except:
			pass

		"""
		# Option 1: Locu Search (obsolete)
		locations = locu_search(query)
		for loc in locations:
			name, locu_id = loc[0], loc[1]
			new_location, created = Location.objects.get_or_create(name=name, locu_id=locu_id)
			if created:
				print(f"Created new id for {name} with locu id of {locu_id}")
		"""
		# Option 2: Foursquare Search
		locations = foursquare_search(query)
		for loc in locations:
			name, four_id = loc[0], loc[1]
			new_location, created = Location.objects.get_or_create(name=name, four_id=four_id)
			if created:
				print(f"Created new id for {name} with foursquare id of {four_id}")

		context['query'] = query
		context['locations'] = locations

	return render(request, 'home.html', context)