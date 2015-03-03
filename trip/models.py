from django.db import models

class Sejour:
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

class Lieu:
	def __init__(self, city, country):
		self.city = city
		self.country = country

class Factory:
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
			UserFactory.users[id_user] = User(id_user)
		return UserFactory.users[id_user]
		

class SejourFactory(Factory):
	sejours = {}

	@classmethod
	def get_sejour(self, id_sejour):
		if id_sejour not in SejourFactory.users:
			SejourFactory.sejours[id_sejour] = Sejour(id_sejour)
		return SejourFactory.sejours[id_sejour]

	@classmethod
	def create_sejour(self, date_debut, date_fin, places, user):
		sejour = Sejour(date_debut, date_fin, places, user)
		SejourFactory.sejours[sejour.getId()] = sejour
		return sejour

class User(models.Model):
	name = models.CharField(max_length=200)
	mail = models.EmailField(max_length=200)

	def __init__(self, id_user):
		self.l = []