import requests

api_key = 'YT6Y5GQKGIgk52DGRSyAxrkDEIQkFNeg'
o = 'BOS'
d = 'LON'
dd = '2016-11-12'
rd = '2016-11-13'
limit = '3'


response = requests.get('http://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?origin={}&destination={}&departure_date={}&return_date={}&number_of_results={}&apikey={}'.format(o, d, dd, rd, limit, api_key));
json_data = response.json()

flight = json_data['results'][0]['itineraries'][0]['outbound']['flights'][0]['aircraft']