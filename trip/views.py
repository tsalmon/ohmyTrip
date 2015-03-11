# -*- coding: UTF-8 -*-

from django.views import generic
from django.shortcuts import render
from . import models

class TripIndex(generic.ListView):
	#queryset = models.Entry.objects.published()
    template_name = "home.html"
    #paginate_by = 2

def index(request):
	return render(request, 'home.html')

"""
def trip(request):
	id_user = 0 # request.POST["id_user"]
	date_debut = 
	user = UserFactory.get_user(0)
	sejour = SejourFactory.create()
	return render(request, 'home.html')
"""
