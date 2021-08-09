from django.db import models


class Geolocation(models.Model):
    lat = models.CharField(max_length=50, blank=True, default=None, null=True)
    lng = models.CharField(max_length=50, default=None, blank=True, null=True)


class Address(models.Model):
    street = models.CharField(max_length=70, blank=True, null=True)
    houseNumber = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    

class Place(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    geolocation = models.ForeignKey(Geolocation, on_delete=models.CASCADE, blank=True, null=True)


class ImageHome(models.Model):
    url = models.URLField(max_length=200, blank=True, null=True)
    

class Home(models.Model):
    description = models.TextField(max_length=500, blank=True, null=True)
    transportation = models.CharField(max_length=200, blank=True, null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ManyToManyField(ImageHome,  blank=True, null=True)
    price = models.IntegerField(default=0, blank=True, null=True)
    environment = models.CharField(max_length=50, blank=True, null=True)
    rooms = models.IntegerField(default=0, blank=True, null=True)
    rank = models.IntegerField(default=0, blank=True, null=True)
    livingArea = models.IntegerField(default=0, blank=True, null=True)
    plotArea = models.IntegerField(default=0, blank=True, null=True)
    kindOfHouse = models.CharField(max_length=50, blank=True, null=True)
    energyLabel = models.CharField(max_length=50, blank=True, null=True)
    constructionYear = models.IntegerField(default=0, blank=True, null=True)
    suitableFor = models.CharField(max_length=50, blank=True, null=True)

