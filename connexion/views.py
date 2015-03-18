from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from trip.user import User

def index(request):
	try:
		user = User.objects.get(mail=request.POST['mail'])
		if user == ObjectDoesNotExist:
			return render(request, 'home.html', {"connect_fail" : True})
		request.session["user"] = user.id
		return render(request, 'home.html', {"connect" : True})
	except ObjectDoesNotExist:
		return render(request, 'home.html', {"connect_fail" : True})
