# -*- coding: UTF-8 -*-

from django.shortcuts import HttpResponse, render
from django.template import Template, Context
from trip.models import UserFactory
from trip.user import User
from trip.place import *
import pprint

def index(request):
	profil_choices = [ "Bar", "Museum", "Park", "Beach", "Skystation", "Restaurant", "NightClub", "Zoo", "Bridge", "Board", "Church", "Landmarks"]
	#pprint.pprint(request.POST)
	firstname = request.POST['firstname'] 
	lastname = request.POST['lastname']
	mail = request.POST['mail']
	password = request.POST["password"]
	profil = {}
	user = UserFactory.create_user(firstname, lastname, mail, password, profil)
	user.save()
	#pprint.pprint(user.getId())
	return render(request, 'home.html', { 'register': True, "profil" : profil_choices, 'user_id' : user.getId()})

def profil(request):
	profil_user = {}
	profil_choices = [ "Bar", "Museum", "Park", "Beach", "SkyStation", "Restaurant", "NightClub", "Zoo", "Bridge", "Board", "Church", "Landmarks"]
	for i in request.POST:
		if i in profil_choices:
			profil_user[eval(i)] = request.POST[i]
	user = User.objects.get(id=request.POST['user'])
	user.setProfil(profil_user)
	request.session['user'] = user.id
	return render(request, "home.html", {'register': True, "has_profil": True})
