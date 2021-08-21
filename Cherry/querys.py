from elasticsearch_dsl.query import Q
from .documents import HomeDocument


def query_builder(must_list, should_list):
    search = HomeDocument.search()
    mustList = []
    shouldList = []

    # make must list query
    for must in must_list:
        mustList.append(Q('match', **{must[0]: must[1]}))
    
    # make should list query
    for should in should_list:
        if should[0] == 'rooms' or should[0] == 'livingArea' or should[0] == 'plotArea' or should[0] == 'constructionYear' :
            mustList.append(Q("range", **{should[0]:{'gte': should[1]}}))

        elif should[0] == 'price':
            shouldList.append(Q("range", price={'lte': should[1]}))

        else:
            shouldList.append(Q('match', **{should[0]: should[1]}))
    
    q = Q('bool', must=mustList, should=shouldList)
    
    return search.query(q)


# separator data(list) to must list, should list, could list
def separator_data(query_list):
    should_list, must_list = [],[]
    for query in query_list:
        if query[1] == 'M':
            must_list.append([query[0],query[2]])

        elif query[1] == 'S' or query[1] == 'should':
            should_list.append([query[0],query[2]])

    return query_builder(must_list, should_list, )


# filter multy data
def filter_data(find_filter, serializers): 
    search = HomeDocument.search()
    query_list = []
    for obj in find_filter:
            
            if obj == 'id' and find_filter[obj] != "":
                filter = serializers.context.get('result')[str(obj)]
                search = search.query("match", id= filter)

                return search
                
            elif obj == 'place.address.street' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                
                if value.find(':'):
                    query_list.append(['place__address__street', value[0], value[2:]])
                    
            elif obj == 'place.address.city' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                
                if value.find(':'):
                    query_list.append(['place__address__city', value[0], value[2:]])
                    
            elif obj == 'place.address.country' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                
                if value.find(':'):
                    query_list.append(['place__address__country', value[0], value[2:]])
              
            elif obj == 'place.address.zipcode' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                
                if value.find(':'):
                    query_list.append(['place__address__zipcode', value[0], value[2:]])
                    
            elif obj == 'place.address.houseNumber' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                
                if value.find(':'):
                    query_list.append(['place__address__houseNumber', value[0], value[2:]])

            elif obj == 'place.geolocation.lat' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])

                if value.find(':'):
                    query_list.append(['place__geolocation__lat', value[0], value[2:]])
                    
            elif obj == 'place.geolocation.lng' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                
                if value.find(':'):
                    query_list.append(['place__geolocation__lng', value[0], value[2:]])
                    
            elif obj == 'price' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                query_list.append(['price', 'should', value])
         
            elif obj == 'environment' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                
                if value.find(':'):
                    query_list.append(['environment', value[0], value[2:]])
                
            elif obj == 'rooms' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                query_list.append(['rooms', 'should', int(value)])
                    
            elif obj == 'livingArea' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                query_list.append(['livingArea', 'should', value])
            
            elif obj == 'plotArea' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                query_list.append(['plotArea', 'should', value])
                    
            if obj == 'kindOfHouse' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                
                if value.find(':'):
                    query_list.append(['kindOfHouse', value[0], value[2:]])
                    
            elif obj == 'energyLabel' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                
                if value.find(':'):
                    query_list.append(['energyLabel', value[0], value[2:]])
                    
            elif obj == 'constructionYear' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                query_list.append(['constructionYear', 'should', value])
                    
                
            elif obj == 'suitableFor' and find_filter[obj] != "":
                value = str(serializers.context.get('result')[str(obj)])
                
                if value.find(':'):
                    query_list.append(['suitableFor', value[0], value[2:]])
                    
    search = separator_data(query_list)
    return search
