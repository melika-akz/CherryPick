
from rest_framework import serializers
from .models import Address, Geolocation, Home, ImageHome, Place
from .documents import HomeDocument


class ImageSerialisers(serializers.ModelSerializer):
    class Meta:
        model = ImageHome
        fields = ('url',)


class GeolocationSerialisers(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = ('lat', 'lon')


class AddressSerialisers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('street', 'houseNumber', 'zipcode', 'city', 'country')


class PlaceSerializers(serializers.ModelSerializer):
    geolocation = GeolocationSerialisers()
    address = AddressSerialisers()
    class Meta:
        model = Place
        fields = ('address', 'geolocation')


class NumberOfSolutionsSerializers(serializers.ModelSerializer):
    radius = serializers.CharField(allow_blank=True)
    id = serializers.CharField()
    place = PlaceSerializers()
    
    class Meta:
        model = Home
        fields = ( 
            # 'callType', 
            'id',
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
            'place',
            'radius'
            )


class ListOfSolutionsSerializers(serializers.ModelSerializer):
    radius = serializers.CharField(allow_blank=True)
    id = serializers.CharField()
    place = PlaceSerializers()
    # image = ImageSerialisers(read_only=True)

    class Meta:
        model = Home
        fields = (  
            # 'callType', 
            'id',
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
            'place',
            'radius'
            )


# post id and get detail of home
class DetailedSolutionSerializers(serializers.ModelSerializer):
    # callType = serializers.CharField(allow_blank=True)
    id = serializers.CharField()
    image = ImageSerialisers(read_only=True)
    description = serializers.CharField(allow_blank=True, read_only=True)
    transportation = serializers.CharField(allow_blank=True, read_only=True)
    place = PlaceSerializers(read_only=True)
    rank =  serializers.IntegerField(read_only=True)

    class Meta:
        model = Home
        fields = [
            'id',
            'description',
            'transportation',
            'place',
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
            'image'
        ]            
        depth = 2

    def create(self, validated_data):
        results = HomeDocument.search().filter("match", id=validated_data['id'])
        url_list = []
        for result in results:
            for img in result['image']:
                urls = img['url']
                url_list.append(urls)
            return  { 
                'id': result['id'],
                'description': result['description'],
                'transportation': result['transportation'], 
                   'place': {
                        'address':{
                        'street': result['place']['address']['street'],
                        'houseNumber': result['place']['address']['houseNumber'],
                        'zipcode': result['place']['address']['zipcode'],
                        'city': result['place']['address']['city'],
                        'country': result['place']['address']['country']},
                        'geolocation': {
                            'lat': result['place']['geolocation']['lat'],
                            'lon': result['place']['geolocation']['lon']
                            },
                        },
                'image': {'url': url_list}, 
                'price': result['price'], 
                'environment': result['environment'], 
                'rooms': result['rooms'], 
                'rank': result['rank'],
                'livingArea': result['livingArea'],
                'plotArea': result['plotArea'],
                'kindOfHouse': result['kindOfHouse'],
                'energyLabel': result['energyLabel'],
                'constructionYear': result['constructionYear'],
                'suitableFor': result['suitableFor'],
                'callType': 'detailedSolution',
                }

        return validated_data
                    
