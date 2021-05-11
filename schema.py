import json
import jsonschema
from jsonschema import validate

dataSchema = {
    #gerekirse her value icin description yazılabilinir
    "description": "DevOps yatayına girecek uygulamaların metadata bilgi seması",    
    "type" : ["object", "string", "integer"], 
    "required" : ["application"],
    "properties" : {        
        "application" : {
            "type" : "object",
            "required" : [ "id" , "business" , "infrastructure" , "software" ],
            "properties" : {
                "id" : {
                    "type" : "integer"
                 },
                "business" : {
                    "type" : "object",
                    "required" : [ "kurulum_saati", "is_birimi"],
                    "properties" : {
                        "kurulum_saati" : {
                            "type" : "integer"  
                        },
                        "is_birimi" : {
                            "type" : "string"
                        }
                    }
                },
                "infrastructure" : {
                    "type" : "object",
                    "required" : [ "sunucu_ismi" , "sunucu_teknoloji" , "middleware" , "direct_DBS" , "db_Tech_Client"],
                    "properties" : {
                        "sunucu_ismi" : {
                            "type" : "string"
                        },
                        "sunucu_teknoloji" : {
                            "type" : "string"
                        },
                        "middleware" : {
                            "type" : "string"
                        },
                        "direct_DBS" : {
                            "type" : "string"
                        },
                        "db_Tech_Client" : {
                            "type" : "string"
                        }
                    }
                },
                "software" : {
                    "type" : "object",
                    "required" : [ "gelistirici", "takim", "takim_direktoru" , "teknoloji", "repository"],
                    "properties" : {
                        "gelistirici" : {
                            "type" : "string"
                        },
                        "takim" : {
                            "type" : "string"
                        },
                        "takim_direktoru" : {
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



#kontrol genişletilecek, türkçe karakter kontrolü eklenecek
def validateJson(jsonData): 
    try :
        validate(instance=jsonData, schema=dataSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True    

def test():
    with open('json_template.txt', 'r') as j:
        jsonData = json.dumps(j.read())
        isValid = validateJson(jsonData)
        if isValid:
            print(jsonData)
            response = "verilen json geçerli"
        else:
            print(jsonData)
            response = "verilen json geçersiz"    
    return response   

