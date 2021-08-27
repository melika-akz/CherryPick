from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from .serializers import (
                        NumberOfSolutionsSerializers, 
                        ListOfSolutionsSerializers, 
                        DetailedSolutionSerializers,
                        )
from .documents import *
from .serializers import HomeDocument
from .querys import filter_data


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
                        'lon': results['place']['geolocation']['lon']        
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
    