from django.db import models

class Sejour(object):
	id_sejour = -1

	def __init__(self, date_begin, date_end, places, user):
		Sejour.id_sejour += 1
		self.date_begin = date_begin
		self.date_end = date_end
		self.places = places
		self.user = user
		self.id = Sejour.id_sejour
		print "create sejour (%d)" % self.id

	def getId(self):
		return self.id

class Factory(object):
	#TODO: make a get() method.
	#		Which allow to get an object in a factory list by inheritance
    def __init__(self, ref):
        self.ref = ref

	@classmethod
	def get(self, list, data, classobject):
		pass

class UserFactory(Factory):
	users = {}

	@classmethod
	def get_user(self, id_user):
		if id_user not in UserFactory.users:
			return Exception("not exist")
		return UserFactory.users[id_user]

	@classmethod
	def create_user(self, firstname, lastname, mail, password, profil):
		user = User(firstname, lastname, mail, password, profil)
		UserFactory.users[user.getId()] = user
		return user


class SejourFactory(Factory):
	sejours = {}

	@classmethod
	def get_sejour(self, id_sejour):
		if id_sejour not in SejourFactory.users:
			return Exception("not exist")
		return SejourFactory.sejours[id_sejour]

	@classmethod
	def create_sejour(self, date_debut, date_fin, places, user):
		sejour = Sejour(date_debut, date_fin, places, user)
		SejourFactory.sejours[sejour.getId()] = sejour
		return sejour
	
class User(models.Model):
	id_user = -1
	name = models.CharField(max_length=200)
	mail = models.EmailField(max_length=200)

	def __init__(self, firstname, lastname, mail, password, profil):
		User.id_user += 1
		self.firstname = firstname
		self.lastname = lastname
		self.mail = mail
		self.password = password
		self.profil = profil
		self.id = User.id_user
		self.profil = Profil(profil)
		print "create user (%d)" % self.id

	def getId(self):
		return self.id

class Profil(object):

	def __init__(self, profil_user):
		self.profil = {}

		for item in profil_user:
			print "%s: %d" % (item, profil_user[item])
			self.profil[item] = eval(item)(profil_user[item])


class Place(object):
	
	def __init__(self, country, local):
		pass

class Region(Place):
	points = [] # Point list

class Point(Place):
	def __init__(self, weight_user):
		self.weight_user = weight_user

class Bar(Point):
	def __init__(self, weight_user):
		super(Bar, self).__init__(weight_user)

class Museum(Point):
	def __init__(self, weight_user):
		super(Museum, self).__init__(weight_user)

class Park(Point):

	def __init__(self, weight_user):
		super(Park, self).__init__(weight_user)

class Beach(Point):
	def __init__(self, weight_user):
		super(Beach, self).__init__(weight_user)

class SkyStation(Point):
	def __init__(self, weight_user):
		super(SkyStation, self).__init__(weight_user)

class Restaurant(Point):
	def __init__(self, weight_user):
		super(Restaurant, self).__init__(weight_user)

class NightClub(Point):
	def __init__(self, weight_user):
		super(NightClub, self).__init__(weight_user)

class Zoo(Point):
	def __init__(self, weight_user):
		super(Zoo, self).__init__(weight_user)

class Bridge(Point):
	def __init__(self, weight_user):
		super(Bridge, self).__init__(weight_user)

class Board(Point):
	def __init__(self, weight_user):
		super(Board, self).__init__(weight_user)