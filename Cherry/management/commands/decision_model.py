from elasticsearch import Elasticsearch
from CherryPick.settings import MEDIA_ROOT
import xlrd
import os
from random import randint

# this mappping for Real State index
mappings= {
  "mappings": {
    "properties": {
      "id": {
      "properties": {
        "datatype": {"type": "text"}, 
        "qualities": {"type": "text"}, 
        "description": {"type": "text"}
          }
        
      },
      "constructionYear": {
        "properties": {
            "datatype": {"type": "text"}, 
            "values": {"type": "text"}, 
            "qualities": {"type": "text"}, 
            "description": {"type": "text"}
            }
      },

      "energyLabel": {
        "properties": {
            "datatype": {"type": "text"}, 
            "values":{"type": "text"}, 
            "qualities":{"type": "text"}, 
            "description":{"type": "text"}
            }
          },
      "environment":{
        "properties":{
          "datatype":{"type": "text"}, 
          "values":{"type": "text"}, 
          "qualities":{"type": "text"}, 
          "description":{"type": "text"}
          }
      },
      "image": {
        "properties": {
          "datatype": {"type": "text"},
          "properties": {
              "url": {"type": "text"}
            }
          
        }
      },

      "kindOfHouse": {
        "properties": {
          "datatype":{"type": "text"}, 
          "values":{"type": "text"}, 
          "qualities":{"type": "text"}, 
          "description":{"type": "text"}
          }
        },

      "livingArea": {
        "properties": {
          "datatype":{"type": "text"}, 
          "values":{"type": "text"}, 
          "qualities":{"type": "text"}, 
          "description":{"type": "text"}
          }
      },
        
      "place": {
        "properties": {
          "datatype": {"type": "text"}, 
          "qualities":{"type": "text"}, 
          "description":{"type": "text"},
          "properties": {
              "address": {
                "properties": {
                  "datatype": {"type": "text"}, 
                  "qualities":{"type": "text"}, 
                  "description":{"type": "text"},
                  "city": {
                        "properties": {
                          "datatype": {"type": "text"}, 
                          "qualities":{"type": "text"}, 
                          "description":{"type": "text"}
                        }
                        
                      },
                  "country": {
                        "properties": {
                          "datatype": {"type": "text"}, 
                          "qualities":{"type": "text"}, 
                          "description":{"type": "text"}
                      }},

                     "houseNumber": {
                        "properties": {
                          "datatype": {"type": "text"}, 
                          "qualities": {"type": "text"}, 
                          "description": {"type": "text"}
                     }},

                     "street":{  
                     "properties": {
                        "datatype": {"type": "text"}, 
                        "qualities": {"type": "text"}, 
                        "description": {"type": "text"}
                      }},

                      "zipcode": {
                        "properties": {
                          "datatype": {"type": "text"}, 
                          "qualities": {"type": "text"}, 
                          "description": {"type": "text"}
                        }
                      } 
                  }
                }
              }                              
            },        
            "geolocation": {
              "properties": {
                "datatype": {"type": "text"}, 
                "qualities":{"type": "text"},
                "description":{"type": "text"},
                  "lat": {
                    "properties": {
                      "datatype": {"type": "text"}, 
                      "qualities":{"type": "text"}, 
                      "description":{"type": "text"}
                    }
                  },
                 "lon": {
                    "properties": {
                      "datatype": {"type": "text"}, 
                      "qualities":{"type": "text"}, 
                      "description":{"type": "text"}
                      }
                    }
                  }
                }
              }
            }
    
    },
      "plotArea": {
        "properties": {
          "datatype":{"type": "text"}, 
          "values":{"type": "text"}, 
          "qualities":{"type": "text"}, 
          "description":{"type": "text"}
            }
        },
      "price": {
        "properties": {
          "datatype": {"type": "text"},
          "qualities":{"type": "text"}, 
          "description":{"type": "text"}
            }
          },
      "rooms": {
        "properties": {
          "datatype": {"type": "text"},
          "values":{"type": "text"},
          "qualities":{"type": "text"},
          "description":{"type": "text"}
        }
      },
      "suitableFor": {
        "properties": {
          "datatype": {"type": "text"}, 
          "values":{"type": "text"}, 
          "qualities":{"type": "text"}, 
          "description":{"type": "text"}
          }
      },
        
      "transportation":{ 
        "properties": { 
          "datatype":{"type": "text"}, 
          "values":{"type": "text"}, 
          "qualities":{"type": "text"}, 
          "description":{"type": "text"}
        }
      }
    }




es = Elasticsearch(host="localhost", port=9200)
es = Elasticsearch("http://elastic:changeme@localhost:9200")

# es.indices.create(index='decision_model', body=mappings)

def creat_realState():
    data={
    "id": {
        "datatype": "unique", 
        "qualities":["N/A"], 
        "description":"desc..."
        },
    "transportation": {
        "datatype": "multivalue", 
        "values":["public","private"], 
        "qualities":["suitability","accessibility","safety"], 
        "description":"desc..."
        },
    "place": {
        "datatype": "string", 
        "qualities":["N/A"], 
        "description":"desc...",
            "address": {
                "datatype": "string", 
                "qualities":["N/A"], 
                "description":"desc...",
                    "street":  {
                        "datatype": "string", 
                        "qualities":["N/A"], 
                        "description":"desc..."},
                    "houseNumber":  {
                        "datatype": "string", 
                        "qualities":["N/A"], 
                        
                        "description":"desc..."},
                    "zipcode":  {
                        "datatype": "string", 
                        "qualities":["N/A"], 
                        "description":"desc..."},
                    "city":  {
                        "datatype": "string", 
                        "qualities":["N/A"], 
                        "description":"desc..."},
                    "country": {
                        "datatype": "string", 
                        "qualities":["N/A"], 
                        "description":"desc..."}
            },
            "geolocation": {
                 "datatype": "geospatial", 
                 "qualities":["locality", "safety", "popularity", "accessibility"],
                 "description":"desc...",
                 
                    "lat": {
                        "datatype": "geospatial", 
                        "qualities":["locality", "safety", "popularity", "accessibility"], 
                        "description":"desc..."},
                    "lon": {
                        "datatype": "geospatial", 
                        "qualities":["locality", "safety", "popularity", "accessibility"], 
                        "description":"desc..."}
                }
    },
    "image": {
        "datatype": "string", 
        "qualities":["N/A"], 
        "description":"desc...",
        "url":  {
          "datatype": "string", 
          "qualities":["N/A"], 
          "description":"desc..."}
    },

    "price":  {"datatype": "monetary", "qualities":["suitability"], "description":"desc..."},
    "environment": {"datatype": "multivalue", "values":["crowded","quite"], "qualities":["suitability", "popularity"], "description":"desc..."},
    "rooms":  {"datatype": "numeric", "values":"range(0,1000)", "qualities":["suitability"], "description":"desc..."},
    "livingArea": {"datatype": "numeric", "values":"range(0,10000)", "qualities":["suitability", "popularity"], "description":"desc..."},
    "plotArea": {"datatype": "numeric", "values":"range(0,10000)", "qualities":["suitability", "popularity"], "description":"desc..."},
    "kindOfHouse": {"datatype": "multivalue", "values":["room","apartment","villa","house"], "qualities":["N/A"], "description":"desc..."},
    "energyLabel":  {"datatype": "multivalue", "values":["A","B","C","D","E","F","G","H"], "qualities":["suitability", "popularity"], "description":"desc..."},
    "constructionYear": {"datatype": "date", "values":"range(1700,Now)", "qualities":["suitability", "popularity"], "description":"desc..."},
    "suitableFor": {"datatype": "multivalue", "values":["family","couple","single"], "qualities":["suitability"], "description":"desc..."},
    "score": {"datatype": "percentage", "values":"range(0,100)", "qualities":["N/A"], "description":"desc..."}
    }
    
    res = es.index(index='decision_model',body=data)