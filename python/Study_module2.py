# 위도 경도 알수있는 패키지
# geopy 

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Jun")
location = geolocator.geocode("Seoul, South Korea")
print(location)