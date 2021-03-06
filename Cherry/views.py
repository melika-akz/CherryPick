from elasticsearch_dsl import index
from rest_framework import response
from CherryPick.documents import client_elasticsearch
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from .serializers import (
                        NumberOfSolutionsSerializers, 
                        ListOfSolutionsSerializers, 
                        DetailedSolutionSerializers,
                        )
from CherryPick.querys import filter_data



def score_building(result_query, count):
    score_data = result_query.execute()
    max_score = result_query.execute().hits.max_score
    score = score_data.hits[count].meta.score
    new_score = (score * 100)/max_score
    
    return int(new_score)

# this func make json-list for listOfSolutions
def list_of_query(result_query):
    list_data = []
    count = 0
    for results in result_query:  
        data = results.to_dict()
        data['score'] = score_building(result_query, count)
        data['callType'] = 'ListOfSolution'
        list_data.append(data)
        count+=1
    
    return list_data


class NumberofSolutionsApiView(CreateAPIView):
    serializer_class = NumberOfSolutionsSerializers
    
    def post(self, request, *args, **kwargs):
        serializers = NumberOfSolutionsSerializers(data=request.data , context= {'result':request.data}, many = True)
        find_filter = serializers.context.get('result')
        result = filter_data(find_filter, serializers)
        # result = list_of_query(result)
        response = result.execute()
        response.hits.total.value

        if serializers.is_valid():
            return Response({'result' :  result.count()})

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
        query = client_elasticsearch('real_estate')
        return query
    

class DetailedSolutionApiView(CreateAPIView):
    serializer_class = DetailedSolutionSerializers
    