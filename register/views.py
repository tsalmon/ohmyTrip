from django.shortcuts import render
from trip.user import User
import pprint

def index(request):
	register = True;
	pprint.pprint(request.POST)
	return render(request, 'home.html', { 'register': register })
