from django.views import generic
from django.shortcuts import render
from . import models


class TripIndex(generic.ListView):
	#queryset = models.Entry.objects.published()
    template_name = "home.html"
    #paginate_by = 2

def index(request):
    return render(request, 'home.html')