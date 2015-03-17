from django.shortcuts import render
from django.core import serializers
from trip.user import User

def index(request):
	user = User.objects.get(mail=request.POST['mail'])
	request.session["user"] = user.id
	return render(request, 'home.html', {"connect" : True})
