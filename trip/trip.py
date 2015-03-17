# -*- coding: UTF-8 -*-

from YelpHelper import query_api as yelp_request
from place import *
try:
    xrange
except:
    xrange = range

class Trip(object):
    """
    
    """
    id_sejour = -1

    def __init__(self, date_begin, date_end, places, user):
        Trip.id_sejour += 1
        self.date_begin = date_begin
        self.date_end = date_end
        self.periode = date_end - date_begin
        self.places = places
        self.user = user
        self.id = Trip.id_sejour
        self.makeTrip()
        print "create trip (%d)" % self.id

    def placesToString(self, liste_place):
        s = ""
        for i in liste_place:
            s += " " + unicode(i)
        print unicode(s)

    def getTripNbDays(self, daily_trip):
        return sum([len(v) for v in daily_trip])

    def makeTrip(self):
        points = self.getPointsActivity()
        daily_trip = self.splitActivityDays(points)
        days_trip = self.getTripNbDays(daily_trip)
        #while(True): TODO?
        if(days_trip > self.periode.days): 
            self.reduceTrip(daily_trip, days_trip)
        elif (days_trip < self.periode.days): 
            self.extendsTrip(daily_trip, days_trip)
        else:
            return days_trip

    def getLonguerTripDay(self, daily_trip, ignore_days = []):
        """
        return index of the longest day in the trip days list city
        """
        duration_trip = [[[len(j)] for j in v] for v in daily_trip ]
        max_day_long_index = 0
        max_day_long_value = duration_trip[0][0]
        max_day_long_city = 0
        for v in range(0, len(duration_trip)):
            for j in range(0, len(duration_trip[v])):
                ignore = (v, j) in ignore_days
                if(not ignore and duration_trip[v][j] > max_day_long_value):
                    max_day_long_index = j
                    max_day_long_value = duration_trip[v][j]
                    max_day_long_city = v

        return [max_day_long_city, max_day_long_index]

    def getShortestTripDay(self, daily_trip, city = None, ignore_days = []):
        """
        return index of the shortest day in the trip days list city
        """
        duration_trip = [[[len(j)] for j in v] for v in daily_trip ]
        min_day_long_index = 0
        min_day_long_value = duration_trip[0][0]
        min_day_long_city = 0
        if(city is not None):
            for j in range(0, len(duration_trip[city])):
                ignore = j in ignore_days
                if(not ignore and duration_trip[city][j] < min_day_long_value):
                    min_day_long_index = j
                    min_day_long_value = duration_trip[city][j]
            return min_day_long_index
        else:
            for v in range(0, len(duration_trip)):
                for j in range(0, len(duration_trip[v])):
                    if(duration_trip[v][j] < min_day_long_value):
                        min_day_long_index = j
                        min_day_long_value = duration_trip[v][j]
                        min_day_long_city = v
            return [min_day_long_city, min_day_long_index]

    def getPointsActivity(self):
        #TODO: delete return
        activite = {}
            
        for p in self.places:   
            activite[p] = []
            for i in self.user.getProfil():
                y = yelp_request(i, p)
                activite[p] += y
        return activite

    def splitActivityDays(self, activite):
        daily_trip = []
        villes = []
        for place in activite:
            liste_place = activite[place]
            jours = []
            jour = 0
            while(len(liste_place) > 0):
                l = self.chooses_items_per_day(liste_place, 720)
                liste_place = [i for i in liste_place if i not in l]
                jours += [l]
                jour += 1
            villes += [jours]
        daily_trip += villes
        return daily_trip

    def reduceTrip(self, daily_trip, nb_days):
        """
        join 2 min days in one while periode > number of days trip
        """
        print "reduce"
        nb_days =  self.getTripNbDays(daily_trip)
        while(nb_days > self.periode.days):
            city, index1 = self.getShortestTripDay(daily_trip)
            index2 = self.getShortestTripDay(daily_trip, city, [index1 ] )
            daily_trip[city][index1] += daily_trip[city][index2]
            del daily_trip[city][index2]
            nb_days =  self.getTripNbDays(daily_trip)
        return daily_trip

    def extendsTrip(self, daily_trip, nb_days):
        """
        split max day in two days while periode > number of days trip
        """
        nb_days =  self.getTripNbDays(daily_trip)
        city, index = self.getLonguerTripDay(daily_trip)

        while(nb_days < self.periode.days and len(daily_trip[city][index]) > 1):
            city, index = self.getLonguerTripDay(daily_trip)
            max_day = daily_trip[city][index]
            events_max_day = max_day[:len(max_day)/2] 
            events_new_day = max_day[len(max_day)/2:]
            daily_trip[city][index] = events_max_day
            daily_trip[city].append(events_new_day)
            nb_days =  self.getTripNbDays(daily_trip)
        return daily_trip
    
    def getId(self):
        return self.id

    def getWeightValuesPlace(self, item):
        time = item.time()
        note_user = int(self.user.profil[item.__class__])
        val = item.value(note_user)

        return [item, time, val]

    def chooses_items_per_day(self, items, time_limit):
        table = [[0]*(time_limit + 1) for j in xrange(len(items) + 1)]
        for j in xrange(1, len(items) + 1):
            item, time, val = self.getWeightValuesPlace(items[j-1])
            for w in xrange(1, time_limit + 1):
                if time > w:
                    table[j][w] = table[j-1][w]
                else:
                    table[j][w] = max(table[j-1][w],
                                      table[j-1][w-time] + val)
        result = []
        w = time_limit
        for j in range(len(items), 0, -1):
            was_added = table[j][w] != table[j-1][w]
     
            if was_added:
                #item, time, val = items[j-1]
                item, time, val = self.getWeightValuesPlace(items[j-1])
                result.append(items[j-1])
                w -= time
     
        return result