from django.db import models


class Geolocation(models.Model):
    id = models.IntegerField(primary_key=True, default=False, null=False)
    lat = models.FloatField(max_length=50, blank=True, default=None, null=True)
    lng = models.FloatField(max_length=50, default=None, blank=True, null=True)


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


class ImageHome(models.Model):
    id = models.IntegerField(primary_key=True, default=False, null=False)
    url = models.URLField(max_length=200, blank=True, null=True)
    

class Home(models.Model):
    id = models.IntegerField(primary_key=True, default=False, null=False)
    description = models.TextField(blank=True, null=True)
    transportation = models.CharField(max_length=200, blank=True, null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ManyToManyField(ImageHome,  blank=True)
    price = models.IntegerField(default=0, blank=True, null=True)
    environment = models.CharField(max_length=100, blank=True, null=True)
    rooms = models.IntegerField(default=0, blank=True, null=True)
    rank = models.IntegerField(default=0, blank=True, null=True)
    livingArea = models.IntegerField(default=0, blank=True, null=True)
    plotArea = models.IntegerField(default=0, blank=True, null=True)
    kindOfHouse = models.CharField(max_length=100, blank=True, null=True)
    energyLabel = models.CharField(max_length=100, blank=True, null=True)
    constructionYear = models.IntegerField(default=0, blank=True, null=True)
    suitableFor = models.CharField(max_length=100, blank=True, null=True)

