# -*- coding: UTF-8 -*-
from django.shortcuts import HttpResponse
from django.views import generic
from django.shortcuts import render
from django import forms
from user import User

class TripIndex(generic.ListView):
	#queryset = models.Entry.objects.published()
    template_name = "home.html"
    #paginate_by = 2

def index(request):
	connected = "member_id" in request.session
	return render(request, 'home.html')

def newtrip(request):
    return render(request, "home.html", {"connect" : True, "newtrip" : True})
