from django.db import models

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
