
from .serializers import HomeDocument
from elasticsearch_dsl import Q

# query building
def filter_data(find_filter, serializers): 
    search = HomeDocument.search()
    for obj in find_filter:
            
            if obj == 'id' and find_filter[obj] != "":
                filter = serializers.context.get('result')[str(obj)]
                search = search.query("match", id= filter)

                return search

            # filter by street
            elif obj == 'place.address.street' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                
                if value.find(':') == 1:
                    if value[0] == 'M':
                        search = search.filter('match',place__address__street=value[2:])

                    elif value[0] == 'S':
                        search = search.filter(Q('match',place__address__street=value[2:]) | ~Q('match',place__address__street=value[2:] ))

                    elif value[0] == 'C':
                        search = search.filter(Q('match',place__address__street=value[2:]) | Q('match',place__address__street="Schotse Hoolglanden" ))

            # filter by city
            elif obj == 'place.address.city' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                
                if value.find(':') == 1:
                    if value[0] == 'M':
                        search = search.filter("match", place__address__city=value[2:])

                    elif value[0] == 'S':
                        search = search.filter(Q("match", place__address__city=value[2:])|~Q("match", place__address__city=value[2:]))

            # filter by country
            elif obj == 'place.address.country' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                if value.find(':') == 1:
                    if value[0] == 'M':
                        search = search.filter("match", place__address__country=value[2:])

                    elif value[0] == 'S':
                        search = search.filter(Q("match", place__address__country=value[2:]) | ~Q("match", place__address__country=value[2:]))

            # filter by zipcode
            elif obj == 'place.address.zipcode' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                
                if value.find(':') == 1:
                    if value[0] == 'M':
                        search = search.filter("match", place__address__zipcode=value[2:])

                    elif value[0] == 'S':
                        search = search.filter(Q("match", place__address__zipcode=value[2:]) | ~Q("match", place__address__zipcode=value[2:]))

            # filter by houseNumber
            elif obj == 'place.address.houseNumber' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                
                if value.find(':') == 1:
                    if value[0] == 'M':
                        search = search.filter("match", place__address__houseNumber=value[2:])

                    elif value[0] == 'S':
                        search = search.filter(Q("match", place__address__houseNumber=value[2:]) | ~Q("match", place__address__houseNumber=value[2:]))

            # filter by lat
            elif obj == 'place.geolocation.lat' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])

                if value.find(':') == 1:
                    if value[0] == 'M':
                        search = search.filter("match", place__geolocation__lat=value[2:])

                    elif value[0] == 'S':
                        search = search.filter(Q("match", place__geolocation__lat=value[2:]) | ~Q("match", place__geolocation__lat=value[2:]))

            # filter by lng
            elif obj == 'place.geolocation.lng' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                
                if value.find(':') == 1:
                    if value[0] == 'M':
                        search = search.filter("match", place__geolocation__lng=value[2:])

                    elif value[0] == 'S':
                        search = search.filter(Q("match", place__geolocation__lng=value[2:]) | ~Q("match", place__geolocation__lng=value[2:]))

            # filter by price
            elif obj == 'price' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                search = search.query("range", price={'lte': value})

            # filter by environment
            elif obj == 'environment' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                
                if value.find(':') == 1:
                    if value[0] == 'M':
                        search = search.filter("match", environment=value[2:])

                    elif value[0] == 'S':
                        search = search.filter(Q("match", environment=value[2:]) | ~Q("match", environment=value[2:]))

            # filter by rooms
            elif obj == 'rooms' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                search = search.query("range", rooms={'gte': value})

            # filter by livingArea
            elif obj == 'livingArea' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                search = search.query("range", livingArea={'gte': value})
            
            #filter by plotArea
            elif obj == 'plotArea' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                search = search.query("range", plotArea={'gte': value})
            
            # filter by kindOfHouse
            if obj == 'kindOfHouse' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                
                if value.find(':') == 1:
                    if value[0] == 'M':
                        search = search.filter("match", kindOfHouse=value[2:])

                    elif value[0] == 'S':
                        search = search.filter(Q("match", kindOfHouse=value[2:]) | ~Q("match", kindOfHouse=value[2:]))

            # filter by energyLabel
            elif obj == 'energyLabel' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                
                if value.find(':') == 1:
                    if value[0] == 'M':
                        search = search.filter("match", energyLabel=value[2:])

                    elif value[0] == 'S':
                        search = search.filter(Q("match", energyLabel=value[2:]) | ~Q("match", energyLabel=value[2:]))

            # filter by constructionYear
            elif obj == 'constructionYear' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                search = search.filter(Q("range", constructionYear={'lte': value}))

            # filter by suitableFor  
            elif obj == 'suitableFor' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                
                if value.find(':') == 1:
                    if value[0] == 'M':
                        search = search.filter("match", suitableFor=value[2:])

                    elif value[0] == 'S':
                        if value[2:] == 'Single':
                            search = search.filter(Q("match", suitableFor=value[2:]) | Q("match", suitableFor="Couple"))

                        elif value[2:] == 'Couple':
                            search = search.filter(Q("match", suitableFor=value[2:]) | Q("match", suitableFor="Family"))
                        
                        search = search.filter(Q("match", suitableFor=value[2:]) | ~Q("match", suitableFor="Family"))
                        
    return search
