from elasticsearch_dsl.function import ScoreFunction
from elasticsearch_dsl.query import Q , MatchAll, MultiMatch, ScriptScore
from .documents import HomeDocument


def make_must_list_query(must_list):
    mustList = []
    for must in must_list:
        if must[0] == 'rooms' or must[0] == 'livingArea' or must[0] == 'plotArea' or must[0] == 'constructionYear' :
            mustList.append(Q("range", **{must[0]:{'gte': must[1]}}))

        elif must[0] == 'price':
            mustList.append(Q("range", price={'lte': must[1]}))

        mustList.append(Q('match', **{must[0]: must[1]}))

    return mustList


def make_should_list_query(should_list, must_list):
    shouldList = []
    for should in should_list:
        
        if should[0] == 'rooms' or should[0] == 'livingArea' or should[0] == 'plotArea' or should[0] == 'constructionYear' :
            shouldList.append(Q("range", **{should[0]:{'gte': should[1]}}))
           
        elif should[0] == 'price':
            shouldList.append(Q("range", price={'lte': should[1]}))
           
        else:
            shouldList.append(Q('match', **{should[0]: should[1]}))
           
    return shouldList


def query_builder(must_list, should_list):
    search = HomeDocument.search()

    # make must list query
    mustList = make_must_list_query(must_list)

    # make should list query
    shouldList = make_should_list_query(should_list, must_list)
    if len(must_list) == 0:
        q = Q('bool', must=MatchAll(), should=shouldList)

    else:
        q = Q('bool', must=mustList, should=shouldList)
    
    search = search.query(q)
    return search

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
    search = HomeDocument.search()
    query_list = []
    for obj in find_filter:
        if obj == 'id' and find_filter[obj] != "":
            filter = serializers.context.get('result')[str(obj)]
            search = search.query("match", id= filter)

            return search

        elif find_filter[obj] != "":
            value = str(serializers.context.get('result')[str(obj)])
                
            if value.find(':'):
                query_list.append([obj, value[0], value[2:]])
                    
    search = separator_data(query_list)
    return search