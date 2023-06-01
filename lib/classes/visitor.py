class Visitor:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._national_parks = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, 'name') and isinstance(name, str) and 1<= len(name) <= 15:
            self._name = name
        else:
            raise Exception

    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        if new_national_park and isinstance(new_national_park, NationalPark):
            self._national_parks.append(new_national_park)
        return list(set(self._national_parks))