import requests
import json

with open('destinations.json') as data_file:    
    POI = json.load(data_file)

def getDestination(attraction):
	return attraction

def getPricing(price):
	if price == 1:
		return "less than $10"
	elif price == 2:
		return "Between $10 and $20"
	elif price == 3:
		return "Between $20 and $30"
	elif price == 4:
		return "Greater than $30"

def getLocation(d):
	venue_location = d['response']['groups'][0]['items'][0]['venue']['location']['formattedAddress'][0]
	return venue_location

def getVenue(d):
	venue_name = d['response']['groups'][0]['items'][0]['venue']['name']
	return venue_name

def getLL():
	response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA')
	resp_json_payload = response.json()
	return (resp_json_payload['results'][0]['geometry']['location'])

def getTransportation(client_id, client_secret, lat, lng, limit, query, price):
	response = requests.get('https://api.foursquare.com/v2/venues/explore?client_id={}&client_secret={}&ll={},{}&v=20161111&m=foursquare&query={}&limit={}&price={}'.format(client_id, client_secret, lat, lng, query, limit, price))
	resp_json_payload =  response.json() 
	venue_name = getVenue(resp_json_payload)
	venue_location = getLocation(resp_json_payload)
	return {'trans_name': venue_name, 'trans_location': venue_location}

def getRestaurant(client_id, client_secret, lat, lng, limit, query, price):
	response = requests.get('https://api.foursquare.com/v2/venues/explore?client_id={}&client_secret={}&ll={},{}&v=20161111&m=foursquare&query={}&limit={}&price={}'.format(client_id, client_secret, lat, lng, query, limit, price))
	resp_json_payload = response.json()
	venue_name = getVenue(resp_json_payload);
	venue_location = getLocation(resp_json_payload)
	return {'restaurant_name': venue_name, 'restaurant_location': venue_location}


#########################################


client_id = 'BAHF1IYXFSMKDXBNDV4U12BGXVPYMOQFAUCQZSSOETLRJH1V'
client_secret = 'WXUBF5O2VROWO1A3NNRFLQUYSPU3BHGWDSPCXB5ES4E0HX1J'
near = 'Mountain View'

ll = getLL()
lat = ll['lat']
lng = ll['lng']

food_queries = ['sushi', 'tacos', 'hamburgers', 'vegan', 'Chinese', 'Chicken', 'Beef', 'Vegetarian']
query = food_queries[4]
limit = 1
price = 1
attraction ='Disneyland Park'

def vacationPlans(data) :
	package = {'destination': getDestination(attraction), 'transportation_info': getTransportation(client_id, client_secret, lat, lng, limit, query, price), 'restaurant_info': getRestaurant(client_id, client_secret, lat, lng, limit, query, price)}
	return package

#########################################

########## Call each method and to return designated values to front end ###########
# print "Here are some location Attractions in: " + near
# print "Venue: " + getVenue(d) 
# print "Address: " + getLocation(d)
# print "Price Range: " + getPricing(price)
# print "-------------------"

# print "Cheapest Car rentals near you: "
# print "Venue name: " + car_rentals['venue_name']
# print "Venue location: " + car_rentals['venue_location']



############################################
# decision = raw_input("Would you like to purchase this package?")
# if decision.lower() == "yes":
# 	print "Awesome!"
# else:
	# print "Thanks for using the App!"