from rest_framework import serializers
from .documents import client_elasticsearch


class ImageSerialisers(serializers.Serializer):
    url = serializers.CharField(allow_blank=True)


class GeolocationSerialisers(serializers.Serializer):
    lat = serializers.CharField(allow_blank=True)
    lon = serializers.CharField(allow_blank=True)
    

class AddressSerialisers(serializers.Serializer):
    street= serializers.CharField(allow_blank=True)
    houseNumber = serializers.CharField(allow_blank=True)
    zipcode = serializers.CharField(allow_blank=True)
    city = serializers.CharField(allow_blank=True)
    country = serializers.CharField(allow_blank=True)

    
class PlaceSerializers(serializers.Serializer):
    geolocation = GeolocationSerialisers()
    address = AddressSerialisers()


class NumberOfSolutionsSerializers(serializers.Serializer):
    id = serializers.CharField(allow_blank=True)
    price = serializers.CharField(allow_blank=True)
    environment = serializers.CharField(allow_blank=True)
    rooms = serializers.CharField(allow_blank=True)
    rank = serializers.CharField(allow_blank=True)
    livingArea = serializers.CharField(allow_blank=True)
    plotArea = serializers.CharField(allow_blank=True)
    kindOfHouse = serializers.CharField(allow_blank=True)
    energyLabel = serializers.CharField(allow_blank=True)
    constructionYear = serializers.CharField(allow_blank=True)
    suitableFor = serializers.CharField(allow_blank=True)
    place = PlaceSerializers()
    radius = serializers.CharField(allow_blank=True)
   

class ListOfSolutionsSerializers(serializers.Serializer):
    id = serializers.CharField(allow_blank=True)
    description = serializers.CharField(allow_blank=True, read_only=True)
    transportation = serializers.CharField(allow_blank=True, read_only=True)
    price = serializers.CharField(allow_blank=True)
    environment = serializers.CharField(allow_blank=True)
    rooms = serializers.CharField(allow_blank=True)
    rank = serializers.CharField(allow_blank=True)
    livingArea = serializers.CharField(allow_blank=True)
    plotArea = serializers.CharField(allow_blank=True)
    kindOfHouse = serializers.CharField(allow_blank=True)
    energyLabel = serializers.CharField(allow_blank=True)
    constructionYear = serializers.CharField(allow_blank=True)
    suitableFor = serializers.CharField(allow_blank=True)
    place = PlaceSerializers()
    radius = serializers.CharField(allow_blank=True)
    image = ImageSerialisers(read_only=True)
    callType = serializers.CharField(allow_blank=True, read_only=True)
    score = serializers.CharField(allow_blank=True, read_only=True)


# post id and get detail of home
class DetailedSolutionSerializers(serializers.Serializer):
    id = serializers.CharField()
    description = serializers.CharField(allow_blank=True, read_only=True)
    transportation = serializers.CharField(allow_blank=True, read_only=True)
    price = serializers.CharField(allow_blank=True)
    environment = serializers.CharField(allow_blank=True)
    rooms = serializers.CharField(allow_blank=True)
    rank = serializers.CharField(allow_blank=True)
    livingArea = serializers.CharField(allow_blank=True)
    plotArea = serializers.CharField(allow_blank=True)
    kindOfHouse = serializers.CharField(allow_blank=True)
    energyLabel = serializers.CharField(allow_blank=True)
    constructionYear = serializers.CharField(allow_blank=True)
    suitableFor = serializers.CharField(allow_blank=True)
    place = PlaceSerializers()
    image = ImageSerialisers(read_only=True)
    
    
    def create(self, validated_data):
        results = client_elasticsearch().filter("match", id=validated_data['id'])
    
        for result in results:
            return result.to_dict()

        return validated_data
                    