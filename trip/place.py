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
	NOTE_MAX = 5.0
	def __init__(self, infos):
		self.infos = infos

	def time(self):
		estimation = self.estimation
		amplitude = self.estimation_amplitude
		note = float(self.infos[u'rating'])
		return int(estimation * amplitude * (note / self.NOTE_MAX))

	def value(self, note_user):
		nb_ratings = self.infos[u'review_count']
		rating = self.infos[u'rating']
		return float(note_user) * ( rating + nb_ratings )

	def __str__(self):
		#TODO: return default string value for a point object
		return u"(%s, %s, %s)" % (self.infos[u"name"], self.infos[u"rating"], self.infos[u"review_count"])

class Bar(Point):
	estimation = 60.0
	estimation_amplitude = 2.5

	def __init__(self, infos):
		super(Bar, self).__init__(infos)

	def __str__(self):
		return "bar = %s" % super(Bar, self).__str__()

class Museum(Point):
	estimation = 120
	estimation_amplitude = 4

	def __init__(self, infos):
		super(Museum, self).__init__(infos)

	def __str__(self):
		return "museum = %s" % super(Museum, self).__str__()

class Park(Point):
	estimation = 45
	estimation_amplitude = 5

	def __init__(self, infos):
		super(Park, self).__init__(infos)

	def __str__(self):
		return "park"

class Beach(Point):
	estimation = 120
	estimation_amplitude = 4

	def __init__(self, infos):
		super(Beach, self).__init__(infos)

	def __str__(self):
		return "beach"

class SkyStation(Point):
	estimation = 120
	estimation_amplitude = 4

	def __init__(self, infos):
		super(SkyStation, self).__init__(infos)

	def __str__(self):
		return "sky"

class Restaurant(Point):
	estimation = 30
	estimation_amplitude = 3

	def __init__(self, infos):
		super(Restaurant, self).__init__(infos)

	def __str__(self):
		return "restaurant"

class NightClub(Point):
	estimation = 300
	estimation_amplitude = 1.5

	def __init__(self, infos):
		super(NightClub, self).__init__(infos)

	def __str__(self):
		return "boite de nuit"

class Zoo(Point):
	estimation = 60
	estimation_amplitude = 1.5

	def __init__(self, infos):
		super(Zoo, self).__init__(infos)

	def __str__(self):
		return "zoo"

class Bridge(Point):
	estimation = 10
	estimation_amplitude = 3

	def __init__(self, infos):
		super(Bridge, self).__init__(infos)

	def __str__(self):
		return "Pont : %s" % super(Bridge, self).__str__()

class Board(Point):
	estimation = 30
	estimation_amplitude = 2

	def __init__(self, infos):
		super(Board, self).__init__(infos)

	def __str__(self):
		return "port"

class LocalFlavor(Point):
	estimation = 60
	estimation_amplitude = 3
	def __init__(self, infos):
		super(LocalFlavor, self).__init__(infos)

	def __str__(self):
		return "localflavor"
