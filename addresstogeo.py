#convert to geo coordinates

from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("175 5th Avenue NYC")
print location.latitude
print location.longitude

