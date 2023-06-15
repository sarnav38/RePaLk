from geopy.geocoders import Nominatim
import geocoder

def getLogLat(add: str) -> str:
    loc = Nominatim(user_agent='Mygeo')
    getad = loc.geocode(add)
    return f'Location Latitude is: {str(getad.latitude)} and Longitude is: {str(getad.longitude)}'

def getIpLoc(ip: str) -> str:
    getIp = geocoder.ip(ip)
    return f'Ip Address Location Latitude is: {str(getIp.latlng[0])} and Longitude is: {str(getIp.latlng[1])}'
