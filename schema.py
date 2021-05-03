import json
import jsonschema
from jsonschema import validate

dataSchema = {
    #gerekirse her value icin description yaz
    "description": "DevOps yatayına girecek uygulamaların metadata bilgi seması",    
    "type" : "object",    
    "properties" : {
        "$defs": {
            "application" : {
                "type" : "object",
                "required" : [ "id" , "business" , "infrastructure" , "software" ],
                "properties" : {
                    "id" : {
                        "type" : "integer"
                    },
                    "business" : {
                        "type" : "object",
                        "required" : [ "kurulumSaati", "isBrimi"],
                        "properties" : {
                            "kurulumSaati" : {
                                "type" : "integer"  #simdilik integer dedim ama hata olabilir
                            },
                            "isBirimi" : {
                                "type" : "string"
                            }
                        }
                    },
                    "infrastructure" : {
                        "type" : "object",
                        "required" : [ "sunucuIsmi" , "sunucuTeknoloji" , "middleware" , "directDBS" , "dbTechClient"],
                        "properties" : {
                            "sunucuIsmi" : {
                                "type" : "string"
                            },
                            "sunucuTeknoloji" : {
                                "type" : "string"
                            },
                            "middleware" : {
                                "type" : "string"
                            },
                            "directDBS" : {
                                "type" : "string"
                            },
                            "dbTechClient" : {
                                "type" : "string"
                            }
                        }
                    },
                    "software" : {
                        "type" : "object",
                        "required" : [ "gelistirici", "takim", "takimDirektoru" , "teknoloji", "repository"],
                        "properties" : {
                            "gelistirici" : {
                                "type" : "string"
                            },
                            "takim" : {
                                "type" : "string"
                            },
                            "takimDirektoru" : {
                                "type" : "string"
                            },
                            "teknoloji" : {
                                "type" : "string"
                            },
                            "repository" : {
                                "type" : "string"
                            }

                        }
                    }
                }
            }
        }
        

        }

    }

}

def validateJson(jsonData):
    try :
        validate(instance=jsonData, schema=dataSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True    

#to use:
#jsonData = json.loads('blablabla')
#isValid = validateJson(jsonData)
#if isValid:
#   print(jsonData)
#   print("verilen json gecerli")
#else:
#   print(jsonData)
#   print("verilen json gecersiz")