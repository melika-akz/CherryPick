from elasticsearch_dsl import index
from elasticsearch_dsl.query import Q , MatchAll
from .documents import client_elasticsearch

# connect to index realstate and send hits
def query_realstate():
    search = client_elasticsearch('decision_model')
    search = search.query(Q('bool', must=MatchAll()))
    data = search.execute().hits[0]

    return data


# check . in str value and separator
def check_point(query):
    # if str obj like place.address.city split 
    if str(query).find('.'):
        query = str(query).split('.')[0]

    return query


# make list of must query
def make_must_list_query(must_list):
    query_type = query_realstate()
    mustList = []

    for must in must_list:
        mst = check_point(must[0])

        if query_type[mst]['datatype'] == 'date' :
            mustList.append(Q("range", **{must[0]:{'gte': must[1]}}))

        elif query_type[mst]['datatype'] == 'numeric':
             mustList.append(Q("range", **{must[0]:{'gte': must[1]}}))

        elif query_type[mst]['datatype'] == 'monetary':
            mustList.append(Q("range", price={'lte': must[1]}))

        elif query_type[mst]['datatype'] == 'multivalue':
            for value in query_type[must[0]]['values']:

                if value == must[1]:
                    mustList.append(Q('match', **{must[0]: must[1]}))

        elif query_type[mst]['datatype'] == 'string':
            mustList.append(Q('match', **{must[0]: must[1]}))

        elif query_type[mst]['datatype'] == 'geospatial':
           mustList.append(Q('match', **{must[0]: must[1]}))

        mustList.append(Q('match', **{must[0]: must[1]}))

    return mustList


# make list of should query
def make_should_list_query(should_list):
    query_type = query_realstate()
    shouldList = []

    for should in should_list:
        shd = check_point(should[0])

        if query_type[shd]['datatype'] == 'date' :
                shouldList.append(Q("range", **{should[0]:{'gte': should[1]}}))

        elif query_type[shd]['datatype'] == 'numeric':
                shouldList.append(Q("range", **{should[0]:{'gte': should[1]}}))

        elif query_type[shd]['datatype'] == 'monetary' :
                shouldList.append(Q("range", price={'lte': should[1]}))
            
        elif query_type[shd]['datatype'] == 'multivalue':
            for value in query_type[should[0]]['values']:       
                if value == should[1]:
                    shouldList.append(Q('match', **{should[0]: should[1]}))

        elif query_type[shd]['datatype'] == 'string':
            shouldList.append(Q('match', **{should[0]: should[1]}))
            
        elif query_type[shd]['datatype'] == 'geospatial':
            shouldList.append(Q('match', **{should[0]: should[1]}))
            
        shouldList.append(Q('match', **{should[0]: should[1]}))
            
    return shouldList


def query_builder(must_list, should_list):
    search = client_elasticsearch('real_estate')
    
    # make must list query
    mustList = make_must_list_query(must_list)

    # make should list query
    shouldList = make_should_list_query(should_list)

    if len(must_list) == 0:
        q = Q('bool', must=MatchAll(), should=shouldList)
        #  filter=Q('geo_distance', distance="3000km", place__geolocation={'lat':"4.88015951",'lon':"51.577141"}))

    else:
        q = Q('bool', must=mustList, should=shouldList)
    
    search = search.query(q)

    return search.extra(track_total_hits=True)


# separator data(list) to must list, should list, could list
def separator_data(query_list):
    should_list, must_list = [],[]

    for query in query_list:
        if query[1] == 'M':
            must_list.append([query[0],query[2]])

        elif query[1] == 'S' or query[1] == 'C':
            should_list.append([query[0],query[2]])

    return query_builder(must_list, should_list)


# filter multy data
def filter_data(find_filter, serializers): 
    query_list = []

    for obj in find_filter:
        if find_filter[obj] != "":
            value = str(serializers.context.get('result')[str(obj)])
            
            if value.find(':'):
                query_list.append([obj, value[0], value[2:]])

    search = separator_data(query_list)
    return search



