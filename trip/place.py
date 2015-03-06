import pprint

class Place(object):
	def __init__(self, name, address=None, coordinate=None):
		self.address = address
		self.coordinate = coordinate
		self.name = name

	def getTypePlace():
		return "toto"

	def __str__(self):
		return ("%s") % (self.name)

	def getLocation(self):
		#TODO
			pass

class Country(Place):
	def __init__(self, country_name):
		self.name = country_name

class City(Place):
	def __init__(self, city_name, country_name, region_name):
		super(City, self).__init__(city_name)
		self.name = city_name
		self.country = Country(country_name)
		self.region = Region(region_name, self.country)

class Region(Place):
	points = [] # Point list

	def __init__(self, region_name, country):
		super(Region, self).__init__(region_name)
		self.name = region_name
		self.country = country

class Point(Place):
	def __init__(self, address, coordinate, name):
		self.address, coordinate, name = address, coordinate, name

	def __str__(self):
		#TODO: return default string value for a point object
		return "point str"

class Bar(Point):

	def __init__(self, address, coordinate, name):
		super(Bar, self).__init__(address, coordinate, name)

	def __str__(self):
		return "bar"

class Museum(Point):
	def __init__(self, address, coordinate, name):
		super(Museum, self).__init__(address, coordinate, name)

	def __str__(self):
		return "musem"

class Park(Point):
	def __init__(self, address, coordinate, name):
		super(Park, self).__init__(address, coordinate, name)

	def __str__(self):
		return "park"

class Beach(Point):
	def __init__(self, address, coordinate, name):
		super(Beach, self).__init__(address, coordinate, name)

	def __str__(self):
		return "beach"

class SkyStation(Point):
	def __init__(self, address, coordinate, name):
		super(SkyStation, self).__init__(address, coordinate, name)

	def __str__(self):
		return "sky"

class Restaurant(Point):
	def __init__(self, address, coordinate, name):
		super(Restaurant, self).__init__(address, coordinate, name)

	def __str__(self):
		return "restaurant"

class NightClub(Point):
	def __init__(self, address, coordinate, name):
		super(NightClub, self).__init__(address, coordinate, name)

	def __str__(self):
		return "boite de nuit"

class Zoo(Point):
	def __init__(self, address, coordinate, name):
		super(Zoo, self).__init__(address, coordinate, name)

	def __str__(self):
		return "zoo"

class Bridge(Point):
	def __init__(self, address, coordinate, name):
		super(Bridge, self).__init__(address, coordinate, name)

	def __str__(self):
		return "pont"

class Board(Point):
	def __init__(self, address, coordinate, name):
		super(Board, self).__init__(address, coordinate, name)

	def __str__(self):
		return "port"
