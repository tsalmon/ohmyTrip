from django.db import models
from place import *
from sejour import Sejour
from user import User
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

