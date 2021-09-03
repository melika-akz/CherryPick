from typing import Dict
from django_elasticsearch_dsl import Document, fields, GeoPoint
from django_elasticsearch_dsl.registries import registry
from .models import Address, Geolocation, Home, ImageHome, Place
# from elasticsearch_dsl import Date, Integer, Keyword, Text, connections, GeoShape, Nested, InnerDoc,GeoPoint
from datetime import datetime



@registry.register_document
class AddressDocument(Document):
    class Index:
        name = 'address'   
        settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }   

    class Django:
        model = Address
        fields = ['id', 'street', 'houseNumber', 'zipcode', 'city', 'country']

@registry.register_document
class ImageDocument(Document):
    class Index:
        name = 'image'   
        settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }   

    class Django:
        model = ImageHome
        fields = ['id', 'url']


@registry.register_document
class GeolocationDocument(Document):
    class Index:
        name = 'geolocation'   
        settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }   

    class Django:
        model = Geolocation
        fields = ['id', 'lat', 'lon']


@registry.register_document
class PlaceDocument(Document):
    class Index:
        name = 'place'   
        settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }   
                    
    class Django:
        model = Place
        fields = ['id']

# class GeolocationX(InnerDoc):
#     lon = fields.FloatField()
#     lat = fields.FloatField()

#     def age(self):
#         return datetime.now()

@registry.register_document
class HomeDocument(Document):
    class Index:
        name = 'cherry'   
        settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }    

    place =  fields.ObjectField(properties={
                    'address': fields.ObjectField(properties={
                        'street': fields.TextField(),
                        'houseNumber':  fields.TextField(),
                        'zipcode':  fields.TextField(),
                        'city':  fields.TextField(),
                        'country':  fields.TextField()}),
                    
                    'geolocation': fields.GeoPoint(fields={'lan':fields.TextField(),'lon':fields.TextField()})
    })
    image = fields.ObjectField(properties={
        'url': fields.TextField(),
         })
   
    class Django:
        model = Home  
        
        fields = ['id',
                   'description', 
                   'transportation', 
                   'price', 
                   'environment', 
                   'rooms', 
                   'rank',
                   'livingArea',
                   'plotArea',
                   'kindOfHouse',
                   'energyLabel',
                   'constructionYear',
                   'suitableFor',
                   ]
        related_models = [Place, ImageHome, Geolocation]
    
    def get_instances_from_related(self, related_instance):
            if isinstance(related_instance, ImageDocument):
                return related_instance.url , related_instance.pk
            elif isinstance(related_instance, GeolocationDocument):
                return related_instance.lat , related_instance.lon , related_instance.pk
            elif isinstance(related_instance, AddressDocument):
                return related_instance.street, related_instance.houseNumber, related_instance.zipcode, related_instance.city, related_instance.country, related_instance.pk
    

    def prepare_geolocation(self, instance: Geolocation)->Dict:
        return {
            'lat': instance.geolocation.x,
            'lon': instance.geolocation.y
        }


# GET /cherry/_search
{
  "query": {
    "bool": {
      "must": {
        "match_all": {}
      },
    "filter": {
    "geo_distance": {
      "distance": "3000km",
      "place.geolocation": {
        "lat": "4.8801595",
        "lon": "51.577141"
      }
    }
  }
}
}}