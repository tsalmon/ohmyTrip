# -*- coding: UTF-8 -*-

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
	def __init__(self, infos):
		self.infos = infos

	def __str__(self):
		#TODO: return default string value for a point object
		return "point str"

class Bar(Point):
	estimation_museum = 60
	estimation_museum_amplitude = 2.5

	def __init__(self, infos):
		super(Bar, self).__init__(infos)

	def __str__(self):
		return "bar"

class Museum(Point):
	estimation_museum = 120
	estimation_museum_amplitude = 4

	def __init__(self, infos):
		super(Museum, self).__init__(infos)

	def __str__(self):
		return "musem"

class Park(Point):
	estimation_park = 45
	estimation_park_amplitude = 5

	def __init__(self, infos):
		super(Park, self).__init__(infos)

	def __str__(self):
		return "park"

class Beach(Point):
	estimation_beach = 120
	estimation_beach_amplitude = 4

	def __init__(self, infos):
		super(Beach, self).__init__(infos)

	def __str__(self):
		return "beach"

class SkyStation(Point):
	estimation_sky = 120
	estimation_sky_amplitude = 4

	def __init__(self, infos):
		super(SkyStation, self).__init__(infos)

	def __str__(self):
		return "sky"

class Restaurant(Point):
	estimation_restaurant = 30
	estimation_restaurant_amplitude = 3

	def __init__(self, infos):
		super(Restaurant, self).__init__(infos)

	def __str__(self):
		return "restaurant"

class NightClub(Point):
	estimation_nightclub = 300
	estimation_nightclub_amplitude = 1.5

	def __init__(self, infos):
		super(NightClub, self).__init__(infos)

	def __str__(self):
		return "boite de nuit"

class Zoo(Point):
	estimation_zoo = 60
	estimation_zoo_amplitude = 1.5

	def __init__(self, infos):
		super(Zoo, self).__init__(infos)

	def __str__(self):
		return "zoo"

class Bridge(Point):
	estimation_bridge = 10
	estimation_bridge_amplitude = 3

	def __init__(self, infos):
		super(Bridge, self).__init__(infos)

	def __str__(self):
		return "pont"

class Board(Point):
	estimation_board = 30
	estimation_board_amplitude = 2

	def __init__(self, infos):
		super(Board, self).__init__(infos)

	def __str__(self):
		return "port"
