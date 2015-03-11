from django.test import TestCase
from datetime import datetime
from models import UserFactory, TripFactory, Place
from place import *
from pprint import pprint as var_dump # PHP...


class TripMethodTests(TestCase):
    def test_new_trip(self):
        """
        make a trip at Paris, Nantes and Brest from 15/07/15 to 03/08/15 
        """
        id_user = 0
        date_debut = datetime(2015, 7, 15)
        date_fin = datetime(2015, 8, 3)

        paris  = City('Paris', "France", "Ile-De-France")
        nantes = City("Nantes", "France", "Pays-de-la-Loire")
        brest  = City("Brest", "France", "Bretagne")
        
        lieux = [paris, nantes, brest]
        
        user = UserFactory.get_user(id_user)
        sejour = TripFactory.create_sejour(date_debut, date_fin, lieux, user)

    def test_create_user(self):
    	"""
    	create a user (just in model not in database)
    	"""
    	profil = {
    		Museum : 1
    	}
    	user = UserFactory.create_user("Salmon", "Thomas", "th_s@hotmail.fr", "mdp", profil)