# -*- coding: UTF-8 -*-

from django.db import models

class User(models.Model):
	id_user = -1
	lastname = models.CharField(max_length=50, default="", null=False)
	firstname = models.CharField(max_length=50, default="", null=False)
	mail = models.EmailField(max_length=70, default="", null=False)
	password = models.CharField(max_length=10, default="", null=False)

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

class Profil(models.Model):
	#TODO: make a class which abstract profil of a user
	user = models.ForeignKey(User)

	def __init__(self, profil_user):
		self.profil = {}

		for item in profil_user:
			self.profil[item] = item(profil_user[item])
