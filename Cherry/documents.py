from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl_drf import filter_backends
from .models import Address, Geolocation, Home, ImageHome, Place




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
        fields = ['id', 'lat', 'lng']

@registry.register_document
class PlaceDocument(Document):
    class Index:
        name = 'place'   
        settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }   
    
        address: fields.ObjectField(properties={
                        'street': fields.TextField(),
                        'houseNumber': fields.TextField(),
                        'zipcode': fields.TextField(),
                        'city': fields.TextField(),
                        'country': fields.TextField()})

        geolocation: fields.ObjectField(properties={
                        'lat': fields.TextField(),
                        'lng': fields.TextField(), 
                    })
                    
    class Django:
        model = Place
        fields = ['id']

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
                        'houseNumber': fields.TextField(),
                        'zipcode': fields.TextField(),
                        'city': fields.TextField(),
                        'country': fields.TextField()}),
                    'geolocation': fields.ObjectField(properties={
                        'lat': fields.TextField(),
                        'lng': fields.TextField(), 
                    }),
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
                return related_instance.lat , related_instance.lng , related_instance.pk
            elif isinstance(related_instance, AddressDocument):
                return related_instance.street, related_instance.houseNumber, related_instance.zipcode, related_instance.city, related_instance.country, related_instance.pk


    