# -*- coding: UTF-8 -*-


from django.db import models
from place import *
from trip import Trip
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
			try:
				u = User.objects.get(id=id_user)
				UserFactory.users[id_user] = u
				return u
			except ObjectDoesNotExist:
				return Exception("not exist")
		return UserFactory.users[id_user]

	@classmethod
	def create_user(self, firstname, lastname, mail, password, profil):
		user = User(firstname=firstname, lastname=lastname, mail=mail, password=password)
		user.save()
		print "create user (%s)" % (user.id)
		UserFactory.users[user.id] = user
		user.setProfil(profil)
		return user


class TripFactory(Factory):
	sejours = {}

	@classmethod
	def get_sejour(self, id_sejour):
		if id_sejour not in TripFactory.users:
			return Exception("not exist")
		return TripFactory.sejours[id_sejour]

	@classmethod
	def create_sejour(self, date_debut, date_fin, places, user):
		sejour = Trip(date_debut, date_fin, places, user)
		TripFactory.sejours[sejour.getId()] = sejour
		return sejour

