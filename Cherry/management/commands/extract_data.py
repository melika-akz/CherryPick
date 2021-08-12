from CherryPick.settings import MEDIA_ROOT
from Cherry.models import Address, Geolocation, Home, ImageHome, Place
import xlrd
import os
from random import randint


# convert price to int
def make_price(price):
    price = str(price).split(".")
    price_convert = ""
    for p in price:
        price_convert = price_convert + p

    return int(price_convert)


def create_Home(description,price,transportation,kindOfHouse,constructionYear,
                livingArea,plotArea,rooms,energyLabel, suitableFor, 
                 houseNumber, street, zipCode, city,url):
    
    x = randint(1111,99999)

    # add address to db
    address, create = Address.objects.update_or_create(id=x,defaults={
                'street': street,
                'houseNumber': houseNumber,
                'zipcode': zipCode,
                'city': city,
                'country': 'Netherlands'})

    # add geolocation to db
    geolocation, create = Geolocation.objects.update_or_create(id=x,defaults={
                        'lat': 0.0,
                        'lng':0.0,
                    })
                    
    address = Address.objects.filter(id=x)
    geolocation = Geolocation.objects.filter(id=x)

    # add place to db
    place, create = Place.objects.update_or_create(id=x ,defaults={
        'address':address[0],
        'geolocation':geolocation[0],
        })

    # add image to db
    image, create = ImageHome.objects.update_or_create(id =x ,defaults={
         'url': url,
    })

    place = Place.objects.filter(id=x)
    image1 = ImageHome.objects.filter(id=x)

    # add home to db
    instanc, create = Home.objects.update_or_create(id =x ,defaults={
        'description': description,
        'transportation': transportation,
        'place': place[0],
        'price':make_price(price),
        'environment':' ',
        'rooms':rooms,
        'rank':0,
        'livingArea':livingArea,
        'plotArea':plotArea,
        'kindOfHouse':kindOfHouse,
        'energyLabel':energyLabel,
        'constructionYear':constructionYear,
        'suitableFor':suitableFor,
         })
    instanc.image.add(image1[0])


def extract_data_excel():
    media_loc=MEDIA_ROOT+'docs'
    for doc in os.listdir(media_loc):
        file = MEDIA_ROOT+'docs/'+doc
        wb = xlrd.open_workbook(file)
        sh = wb.sheet_by_index(0)
        for rx in range(sh.nrows):
            data = sh.row(rx)
            home_data = data
            create_Home(
                    home_data[0].value,home_data[1].value,home_data[2].value,
                    home_data[3].value,home_data[4].value,home_data[5].value,
                    home_data[6].value,home_data[7].value,home_data[8].value,
                    home_data[9].value,home_data[10].value,home_data[11].value,
                    home_data[12].value,home_data[13].value,home_data[14].value)


