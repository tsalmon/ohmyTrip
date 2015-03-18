# -*- coding: UTF-8 -*-
from django.shortcuts import HttpResponse
from django.views import generic
from datetime import datetime
from django.shortcuts import render
from django import forms
from user import User
from models import TripFactory, UserFactory
from place import City

class TripIndex(generic.ListView):
	#queryset = models.Entry.objects.published()
    template_name = "home.html"
    #paginate_by = 2

def index(request):
	connected = "member_id" in request.session
	return render(request, 'home.html')

def newtrip(request):
	start = request.POST["start_trip"].split("-")
	end = request.POST["end_trip"].split("-")

	start = datetime(int(start[0]), int(start[1]), int(start[2]))
	end = datetime(int(end[0]), int(end[1]), int(end[2]))

	lieu = [City(request.POST["city"], request.POST["region"], request.POST["country"])]
	user = UserFactory.get_user(request.session["user"])
	sejour = TripFactory.create_sejour(start, end, lieu, user)
	return render(request, "home.html", {"connect" : True, "newtrip" : True, "sejour": sejour.getTrip()})
