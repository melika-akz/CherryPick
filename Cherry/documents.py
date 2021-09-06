from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


def client_elasticsearch(index_name):
    es = Elasticsearch(host="localhost", port=9200)
    es = Elasticsearch("http://elastic:changeme@localhost:9200")
    search = es.search(index=index_name)
    if index_name == 'cherry':
        search = Search(index=index_name)
        return search
        
    elif index_name == 'realstate':
        search = Search(index=index_name)
        return search
    