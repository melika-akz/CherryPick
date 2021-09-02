from .models import Geolocation
from math import sin, cos, sqrt, atan2, radians

def calcute_distance(lat, lon, radius):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat)
    lon1 = radians(lon)

    
    geos = Geolocation.objects.all()
    geo_list = []
    distance_l = []
    for geo in geos.values():
        lat2 = radians(float(geo['lat']))
        lon2 = radians(float(geo['lon']))

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        
        if int(distance) <= radius:
            distance = R * c
            geo_list.append([lat2, lon2, distance])
            distance_l.append(distance)
            
            
    
    distance_l.sort(reverse=True)
    print(distance_l)
    print(geo_list)
    for g in geo_list:
        if g[2] == (distance_l[0]):
            return g