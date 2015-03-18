# -*- coding: UTF-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

class User(models.Model):
	lastname = models.CharField(max_length=50, default="", null=False)
	firstname = models.CharField(max_length=50, default="", null=False)
	mail = models.EmailField(max_length=70, default="", null=False, unique=True)
	password = models.CharField(max_length=10, default="", null=False)

	def __str__(self):
		return self.mail

	"""
	def __init__(self, firstname, lastname, mail, password, profil):
		super(lastname=lastname, firstname=firstname, mail=mail, password=password)
		User.id_user += 1
		self.firstname = firstname
		self.lastname = lastname
		self.mail = mail
		self.password = password
		self.profil = profil
		self.id = User.id_user
		self.profil = profil
		print "create user (%d)" % self.id
	"""
	def getId(self):
		return self.id

	def getSelf(self):
		return self

	def setProfil(self, p):
		self.profil = p
		return 
		#p = Profil.objects.get(user=request.POST['mail'])
		try:
			self.profil = Profil.objects.get(user=self)
		except ObjectDoesNotExist:
			d = {}
			print p
			for item in p:
				d[item.__name__.lower()] = int(p[item])
			print d
			self.profil = Profil(user=self, **d)
			#self.profil.save()

	def getProfil(self):
		return self.profil

	def getInteret(self, place):
		return self.profil[place]

class Profil(models.Model):
	#TODO: make a class which abstract profil of a user
	user = models.ForeignKey(User)
	bar = models.SmallIntegerField()
	museum = models.SmallIntegerField()
	park = models.SmallIntegerField()
	beach = models.SmallIntegerField()
	skystation = models.SmallIntegerField()
	restaurant= models.SmallIntegerField()
	nightclub= models.SmallIntegerField()
	zoo= models.SmallIntegerField()
	bridge= models.SmallIntegerField()
	board= models.SmallIntegerField()
	church= models.SmallIntegerField()
	landmarks= models.SmallIntegerField()
