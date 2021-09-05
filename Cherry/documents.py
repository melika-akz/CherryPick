from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, index


def client_elasticsearch():
    es = Elasticsearch(host="localhost", port=9200)
    es = Elasticsearch("http://elastic:changeme@localhost:9200")
    search = es.search(index="realstate")
    search = Search(index='realstate')
    return search