from django.shortcuts import render
from trip.models import UserFactory
import pprint

def index(request):
	register = True;
	pprint.pprint(request.POST)
	firstname = request.POST['firstname'] 
	lastname = request.POST['lastname']
	mail = request.POST['mail']
	password = request.POST["password"]
	profil = {}
	user = UserFactory.create_user(firstname, lastname, mail, password, profil)
	return render(request, 'home.html', { 'register': register })