import xml.etree.ElementTree as ET
import urllib.request as ur

class Flight(object):
    def __init__(self, price, currency, people,  link, agent, leg):
        self.price = price*people
        self.currency = currency
        self.link = link
        self.agent = agent
        self.leg = leg

    def agent_info(self):
        return "Agent #{} - {}".format(self.agent.id, self.agent.name)

    def leg_info(self):
        return "Flight #{} from {} to {}".format(self.leg.number, self.leg.origin(), self.leg.destination())

    def __str__(self):
        line = self.leg_info()
        line += ' costs {} {}'.format(self.price, self.currency)
        return line


class Agent(object):
    def __init__(self, id, name, url):
        self.id = id
        self.name = name
        self.url = url


class Agents(object):
    def __init__(self, agents):
        self.agents = agents
    
    def by_id(self, id):
        agent = list(filter(lamda x: x.id == id, self.agents))
        return agent[0]

class Leg(object):
    def __init__(self, id, number, origin_stat, destin_stat, places):
        self.id = id
        self.number = number
        self.origin_stat = origin_stat
        self.destin_stat = destin_stat
        self.places = places

    def origin(self):
        return self.places.city_name(self.origin_stat)

    def destination(self):
        return self.places.city_name(self.destin_stat)


class Legs(object):
    def __init__(self, legs):
        self.legs = legs
    
    def by_id(self, id):
        for leg in self.legs:
            if leg.id == id:
                return leg

class Place(object):
    def __init__(self, id, code, parentid=0):
        self.id = id
        self.parentid = parentid
        self.code = code
        self.name = None
    
        


class Places(object):
    def __init__(self, places, key):
        self.places = places
        self.__key = key

    def by_id(self, id):
        for place in self.places:
            if place.id == id:
                return place

    def city_name(self, id):
        
        airport = self.by_id(id)
        city = None
        for city in self.places:
            if city.id == airport.parentid:
                break
        for country in self.places:
            if country.id == city.parentid:
                break
        url = 'http://partners.api.skyscanner.net/apiservices/autosuggest/v1.0/RU/GBP/en?id='+airport.code+'-sky&apiKey='+self.__key
        r = eval(ur.urlopen(url).read().decode('utf8'))
        return r['Places'][0]['PlaceName']
    
class Pilot():
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.flight = None
        
    def set_flight(flight_id):
        self.flight = flight_id
        
    def unset_flight():
        if self.flight is not None:
            self.flight = None
 
