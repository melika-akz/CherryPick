from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, index


def client_elasticsearch(index_name):
    es = Elasticsearch(host="localhost", port=9200)
    es = Elasticsearch("http://elastic:changeme@localhost:9200")
    search = es.search(index="realstate")
    if index_name == 'realstate':
        search = Search(index=index_name)
        return search
        
    else:
        search = Search(index=index_name)
        return search