from elasticsearch import Elasticsearch
from CherryPick.settings import MEDIA_ROOT
import xlrd
import os
from random import randint

# this mappping for Real State index
mappings= {
  "mappings":{
      "properties":{
        "constructionYear": {
          "type": "text"
        },
        "description": {
          "type": "text"
        },
        "energyLabel": {
          "type": "text"
        },
        "environment": {
          "type": "text"
        },
        "id": {
          "type": "integer"
        },
        "image": {
          "properties": {
            "url": {
              "type": "text"
            }
          }
        },
        "kindOfHouse": {
          "type": "text"
        },
        "livingArea": {
          "type": "text"
        },
        "place": {
          "properties": {
            "address": {
              "properties": {
                "city": {
                  "type": "text"
                },
                "country": {
                  "type": "text"
                },
                "houseNumber": {
                  "type": "text"
                },
                "street": {
                  "type": "text"
                },
                "zipcode": {
                  "type": "text"
                }
              }
            },
            "geolocation": {
              "type": "geo_point",
               
            }
            
          }
        },
        "plotArea": {
          "type": "text"
        },
        "price": {
          "type": "text"
        },
        "rank": {
          "type": "text"
        },
        "rooms": {
          "type": "text"
        },
        "suitableFor": {
          "type": "text"
        },
        "transportation": {
          "type": "text"
        }
      }
  }}


es = Elasticsearch(host="localhost", port=9200)
es = Elasticsearch("http://elastic:changeme@localhost:9200")


# es.indices.create(index='cherry', body=mappings)


def insert_data(id,description, price, transportation, kindOfHouse, constructionYear,
                livingArea, plotArea, rooms, energyLabel, suitableFor, 
                 houseNumber, street, zipCode, city, url, lon, lat):
    data = {
        "id": id,
        "constructionYear": constructionYear,
        "description": description,
        "energyLabel": energyLabel,
        "environment": "",
        
        "image": {
            "url":[url] 
        },
        "kindOfHouse": kindOfHouse,
        "livingArea": livingArea,
        "place": {
            "address": {
                "city": city,
                "country": "Netherlands",
                "houseNumber": houseNumber,
                "street": street,
                "zipcode": zipCode 
            },
            "geolocation": {
              "lat":lat,
              "lon":lon               
          }
        },
        "plotArea": plotArea,
        "price": price,
        "rank": "",
        "rooms": rooms,
        "suitableFor": suitableFor,
        "transportation": transportation
      }
    

    res = es.index(index='realstate',body=data, )
    print('data'+str(id)+'complete.')

    
def extract_excel():
    media_loc=MEDIA_ROOT+'docs'
    for doc in os.listdir(media_loc):
        file = MEDIA_ROOT+'docs/'+doc
        wb = xlrd.open_workbook(file)
        sh = wb.sheet_by_index(0)
        count = 1
        for rx in range(sh.nrows):
            id = count
            data = sh.row(rx)
            home_data = data
            insert_data(id,
                    home_data[0].value, home_data[1].value, home_data[2].value,
                    home_data[3].value, home_data[4].value, home_data[5].value,
                    home_data[6].value, home_data[7].value, home_data[8].value,
                    home_data[9].value, home_data[10].value, home_data[11].value,
                    home_data[12].value, home_data[13].value, home_data[14].value,
                    home_data[15].value, home_data[16].value)
            count+=1