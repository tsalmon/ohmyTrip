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

def login(request):
    if request.method == 'POST':
        m = Users.objects.get(username=request.POST['username'])
        if m.password == request.POST['password']:
            request.session['member_id'] = m.id
            return HttpResponse("You're logged in.")
        else:
            return HttpResponse("Your username and password didn't match.")
    else :
        form = LogginForm()
        return render_to_response('loggin/index.html', { 'form': form, }, context_instance=RequestContext(request))

"""
def trip(request):
	id_user = 0 # request.POST["id_user"]
	date_debut = 
	user = UserFactory.get_user(0)
	sejour = SejourFactory.create()
	return render(request, 'home.html')
"""
