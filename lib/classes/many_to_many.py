class NationalPark:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, "name"):
            if isinstance(name, str) and len(name) in range(1,15):
                self._name = name
        
    def trips(self):
        trips = []
        for trip in Trip.all:
            if trip.national_park == self:
                trips.append(trip)
        return trips
    
    def visitors(self):
        visitors = []
        for trip in Trip.all:
            if trip.national_park == self:
                if trip.visitor not in visitors:
                    visitors.append(trip.visitor)
        return visitors
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitors = {}
        for trip in Trip.all:
            if trip.national_park == self:
                if trip.visitor not in visitors:
                    visitors.update({trip.visitor : 1})
                else:
                    visitors[trip.visitor] += 1
        print(visitors)
        max_key = max(visitors, key=lambda k: visitors[k])
        return max_key


class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self._visitor = visitor
        self._national_park = national_park
        self._start_date = start_date
        self._end_date = end_date
        Trip.all.append(self)

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date
        # Is in the format "September 1st"

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date
        # Is in the format "September 1st"



class Visitor:

    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) in range(1,15):
            self._name = name


    def trips(self):
        trips = []
        for trip in Trip.all:
            if trip.visitor == self:
                trips.append(trip)
        return trips
    
    def national_parks(self):
        parks = []
        for trip in Trip.all:
            if trip.visitor == self:
                if trip.national_park not in parks:
                    parks.append(trip.national_park)
        print(parks)
        return parks
        
    
    def total_visits_at_park(self, park):
        pass