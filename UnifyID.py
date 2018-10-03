from pyipinfoio import pyipinfoio as py
from math import cos, asin, sqrt, radians, sin

# #haversine formula
# def distance(lat1, lon1, lat2, lon2):
#     p = 0.017453292519943295    
#     a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
#     return ((12742 * asin(sqrt(a))) * .621371)

def haversine(lon1, lat1, lon2, lat2):

    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 3956 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

def getListofInputs():
	ret = []
	with open('/home/aarsh/Desktop/unifyID/inputs', 'r') as fp:
		line = fp.readline()
		while line:
			identifier = line[0:5]
			rest_of_string = line[6:]
			location = ip.lookup(rest_of_string)
			longitude, latitude = [x.strip() for x in location['loc'].split(',')]
			ret.append(Node(location['ip'], longitude, latitude, location['city'], identifier))
			line = fp.readline()
	ret = ret[0: len(ret)-1]
	return ret
			
def findClosest(inputIP, list_of_locations):
	closest = ''
	dist = float("inf")
	inputIPInfo = ip.lookup(inputIP)
	longitude, latitude = [x.strip() for x in inputIPInfo['loc'].split(',')]
	print(latitude, longitude)
	# InputIPInfonode = Node(inputIPInfo['ip'], longitude, latitude, inputIPInfo['city'])
	for x in list_of_locations:
		distanceToCheck = haversine(float(latitude), float(longitude), float(x.lat), float(x.long))
		print(x.cityName)
		print(distanceToCheck)
		if distanceToCheck < dist:
			closest = x
			dist = distanceToCheck

	return(dist, closest)

def getScore(distance, identifier):
	if identifier == "FRAUD":
		return distance * 2
	else:
		return distance

class Node:

	def __init__(self, IPAddress, longitude, lat, cityName, identifier=None, closest=None):
		self.ipaddress = IPAddress
		self.long = longitude
		self.lat = lat
		self.cityName = cityName
		self.identifier = identifier
		self.closest = closest

ip = py.IPLookup()
list_of_locations = getListofInputs()
with open('/home/aarsh/Desktop/unifyID/new_request', 'r') as fp:
	temp = fp.readline()
	print(temp)
distance, closestIPaddresslocation = findClosest(temp, list_of_locations)
print(closestIPaddresslocation.cityName)
print("finalscore: ", getScore(distance, closestIPaddresslocation.identifier))