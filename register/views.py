from django.shortcuts import render
from django.template import Template, Context
from trip.models import UserFactory
import pprint

def index(request):
	#pprint.pprint(request.POST)
	firstname = request.POST['firstname'] 
	lastname = request.POST['lastname']
	mail = request.POST['mail']
	password = request.POST["password"]
	profil = {}
	user = UserFactory.create_user(firstname, lastname, mail, password, profil)
	#pprint.pprint(user.getId())
	profil_choices = [ "bar", "Museum", "Park", "Beach", "Skystation", "Restaurant", "NightClub", "Zoo", "Bridge", "Board", "Church", "Landmarks"]
	return render(request, 'home.html', { 'register': True, "profil" : profil_choices, })