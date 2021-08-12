from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from .serializers import (
                        NumberOfSolutionsSerializers, 
                        ListOfSolutionsSerializers, 
                        DetailedSolutionSerializers,
                        )
from .documents import *
from .serializers import HomeDocument

# filter multy data
def filter_data(find_filter, serializers): 
    search = HomeDocument.search()
    for obj in find_filter:
            
            if obj == 'id' and find_filter[obj] != "":
                filter = serializers.context.get('result')[str(obj)]
                search = search.filter("match", id= filter)
            
            elif obj == 'place.address.street' and find_filter[obj] != "":
                filter = serializers.context.get('result')[str(obj)]
                search = search.filter("match", place__address__street= 'freshte')

            if obj == 'place.address.city' and find_filter[obj] != "":
                filter = serializers.context.get('result')[str(obj)]
                search = search.filter("match", place__address__city= filter)

            elif obj == 'place.address.country' and find_filter[obj] != "":
                filter = serializers.context.get('result')[str(obj)]
                search = search.filter("match", place__address__country= filter)
            
            elif obj == 'place.geolocation.lat' and find_filter[obj] != "":
                filter = serializers.context.get('result')[str(obj)]
                search = search.filter("match", place__geolocation__lat= filter)
            
            elif obj == 'place.geolocation.lng' and find_filter[obj] != "":
                filter = serializers.context.get('result')[str(obj)]
                search = search.filter("match", place__geolocation__lng= filter)
            
            elif obj == 'price' and find_filter[obj] != "":
                filter = serializers.context.get('result')[str(obj)]
                search = search.filter("match", price=filter)
            
            elif obj == 'environment' and find_filter[obj] != "":
                filter = serializers.context.get('result')[str(obj)]
                search = search.filter("match", environment=filter)
            
            elif obj == 'rooms' and find_filter[obj] != "":
                filter = serializers.context.get('result')[str(obj)]
                search = search.filter("match", rooms=filter)
            
            elif obj == 'livingArea' and find_filter[obj] != "":
                filter = serializers.context.get('result')[str(obj)]
                search = search.filter("match", livingArea=filter)
            
            elif obj == 'plotArea' and find_filter[obj] != "":
                filter = serializers.context.get('result')[str(obj)]
                search = search.filter("match", plotArea=filter)
            
            if obj == 'kindOfHouse' and find_filter[obj] != "":
                filter = serializers.context.get('result')[str(obj)]
                search = search.filter("match", kindOfHouse=filter)
            
            elif obj == 'energyLabel' and find_filter[obj] != "":
                filter = serializers.context.get('result')[str(obj)]
                search = search.filter("match", energyLabel=filter)
            
            elif obj == 'constructionYear' and find_filter[obj] != "":
                filter = serializers.context.get('result')[str(obj)]
                search = search.filter("match", constructionYear=filter)
            
            elif obj == 'suitableFor' and find_filter[obj] != "":
                filter = serializers.context.get('result')[str(obj)]
                search = search.filter("match", suitableFor=filter)

            elif obj == 'plotArea' and find_filter[obj] != "":
                filter = serializers.context.get('result')[str(obj)]
                search = search.filter("match", plotArea=filter)
    
    return search

# this func make json-list for listOfSolutions
def list_of_query(data):
    list_data = []
    
    for results in data:
        for img in results['image']:
            urls = img['url']
            
        data = {   
            'id': results['id'],
            'transportation': results['transportation'],
            'place': {
                    'address': {
                    'street': results['place']['address']['street'],
                    'houseNumber':results['place']['address']['houseNumber'],
                    'zipcode':results['place']['address']['zipcode'],
                    'city': results['place']['address']['city'],
                    'country': results['place']['address']['country'],
                    },

                    'geolocation':{
                        'lat': results['place']['geolocation']['lat'],
                        'lng': results['place']['geolocation']['lng']        
                         }
                    },
            'image': {'url': urls,},
            'price': results['price'], 
            'environment': results['environment'], 
            'rooms': results['rooms'], 
            'livingArea': results['livingArea'],
            'plotArea': results['plotArea'],
            'kindOfHouse': results['kindOfHouse'],
            'energyLabel': results['energyLabel'],
            'constructionYear': results['constructionYear'],
            'suitableFor': results['suitableFor'],
            'callType': 'ListOfSolution',
                }
        list_data.append(data)

    return list_data


class NumberofSolutionsApiView(CreateAPIView):
    serializer_class = NumberOfSolutionsSerializers
    
    def post(self, request, *args, **kwargs):
        serializers = NumberOfSolutionsSerializers(data=request.data , context= {'result':request.data}, many = True)
        find_filter = serializers.context.get('result')
        result = filter_data(find_filter, serializers)

        
        if serializers.is_valid():
            return Response({'result' : result.count()})

        return Response()


class listofSolutionsApiView(ListCreateAPIView):
    serializer_class = ListOfSolutionsSerializers
   
    def post(self, request, *args, **kwargs):
        serializers = ListOfSolutionsSerializers(data=request.data , context= {'result':request.data}, many = True)
        find_filter = serializers.context.get('result')
        result = filter_data(find_filter, serializers)
        result = list_of_query(result)
        
        if serializers.is_valid():
            return Response(result)

        return Response()

    def get_queryset(self):
        query =  HomeDocument.search()
        return query
    

class DetailedSolutionApiView(CreateAPIView):
    serializer_class = DetailedSolutionSerializers
    