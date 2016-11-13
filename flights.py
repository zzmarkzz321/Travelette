import requests, ast, collections, json
from amadeus import Flights

api_key = 'M9VCf7kx31dAGysqavyLIAwJfbrnkUV1'
fly = Flights(api_key)

def flight_data(data, org):
	airline = requests.get('https://api.sandbox.amadeus.com/v1.2/travel-intelligence/airline-autocomplete?apikey={}&term={}'.format(api_key, data['airline'])).json()
	data['airline_name'] = airline[0]['label'] if isinstance(airline, list) and airline[0]['value'] == data['airline'] else data['airline']
	data['origin'] = org
	data['book_url'] = 'https://www.google.com/flights/#search;f={origin};t={destination};d={departure_date};r={return_date};a={airline}'.format(**data)
	return data

def get_hotels(flight, rad=25, cnt=3):
	hotels =  requests.get('https://api.sandbox.amadeus.com/v1.2/hotels/search-airport?apikey={}&location={}&check_in={}&check_out={}&radius={}&number_of_results={}'.format(api_key, flight['destination'], flight['departure_date'], flight['return_date'], rad, cnt)).json().get('results')
	return hotels[:cnt]

def get_flights(org, dat, prc, dur='3--10', cnt=3):
	inspiration = fly.inspiration_search(
		origin=org, departure_date=dat, max_price=prc, duration=dur)

	if inspiration.get('status'):
		return None

	flights = collections.OrderedDict(sorted({f['price'].replace('.','')+f['destination']: flight_data(f, org) for f in inspiration.get('results')[:cnt]}.items()))
	for f in flights:
		flights[f]['hotels'] = get_hotels(flights[f])
	return flights
