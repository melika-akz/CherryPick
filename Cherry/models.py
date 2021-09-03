from django.db import models
from django.contrib.gis.db.models import PointField
from elasticsearch_dsl import Date, Integer, Keyword, Text, connections, GeoShape, GeoPoint

class Geolocation(models.Model):
    id = models.IntegerField(primary_key=True, default=False, null=False)
    lat = models.DecimalField(null=True, blank=True, decimal_places=15, max_digits=19, default=0)
    lon = models.DecimalField(null=True, blank=True, decimal_places=15, max_digits=19, default=0)


class Address(models.Model):
    id = models.IntegerField(primary_key=True, default=False, null=False)
    street = models.CharField(max_length=70, blank=True, null=True)
    houseNumber = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    
class Place(models.Model):
    id = models.IntegerField(primary_key=True, default=False, null=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    geolocation = models.ForeignKey(Geolocation, on_delete=models.CASCADE, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)


class ImageHome(models.Model):
    id = models.IntegerField(primary_key=True, default=False, null=False)
    url = models.URLField(max_length=200, blank=True, null=True)
    

class Home(models.Model):
    id = models.IntegerField(primary_key=True, default=False, null=False)
    description = models.TextField(blank=True, null=True)
    transportation = models.CharField(max_length=200, blank=True, null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ManyToManyField(ImageHome,  blank=True)
    price = models.CharField(max_length=100, default=0, blank=True, null=True)
    environment = models.CharField(max_length=100, blank=True, null=True)
    rooms = models.CharField(max_length=100, default=0, blank=True, null=True)
    rank = models.CharField(max_length=100, default=0, blank=True, null=True)
    livingArea = models.CharField(max_length=100, default=0, blank=True, null=True)
    plotArea = models.CharField(max_length=100, default=0, blank=True, null=True)
    kindOfHouse = models.CharField(max_length=100, blank=True, null=True)
    energyLabel = models.CharField(max_length=100, blank=True, null=True)
    constructionYear = models.CharField(max_length=100, default=0, blank=True, null=True)
    suitableFor = models.CharField(max_length=100, blank=True, null=True)

