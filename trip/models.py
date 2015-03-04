from django.db import models
from place import *
from sejour import Sejour
from pprint import pprint as var_dump

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
		self.profil = profil
		print "create user (%d)" % self.id

	def getId(self):
		return self.id

	def getProfil(self):
		return self.profil

	def getInteret(self, place):
		return self.profil[place]

class Profil(object):
	#TODO: make a class which abstract profil of a user
	def __init__(self, profil_user):
		self.profil = {}

		for item in profil_user:
			self.profil[item] = item(profil_user[item])


