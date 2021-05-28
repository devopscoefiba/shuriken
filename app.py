from flask import Flask, redirect, render_template, request
from flask_mongoengine import MongoEngine
from models.post import Post
from utils import *
import templates, settings
from schema import * 
from logging import raiseExceptions
from os import error
from bson import json_util

# define flask as app


app = Flask(__name__)


#   redirect lost people to home :)
@app.route('/')
def go_home():
    return redirect('/home')


#   home route where the magic happens
@app.route('/home', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        post_value = request.form['name']
        temp_json = {
            "value": post_value
        }
        new_post = Post(json_value=temp_json)
        insert_post(new_post)
        return redirect('/home')
    else:
        return render_template('home.html', posts=db.posts.find())


@app.route('/insert/', methods=['POST'])
def insert_post_page():
    return 'inserted'


@app.route('/delete/<_id>', methods=['DELETE'])
def delete_post_page(_id):
    delete_post(int(_id))

    return 'deleted'


@app.route('/update/<_id>', methods=['PUT'])
def update_post_page(_id):
    json_value = request.get_json()
    # update_post(_id, json_value)

    return "updated"

#to check whether given json schema is valid and print error messages if any
@app.route('/test')
def test():
    with open('json_template.txt', 'r') as j:
        t = []
        for lines in j:
            t.append(lines)
        
        jsonData = json.loads(''.join([str(elt) for elt in t ]))    

        isValid = validateJson(jsonData)
        if isValid:
            print(jsonData)
            response = "verilen json geçerli"
        else:
            v = Draft7Validator(dataSchema)  
            errors = sorted(v.iter_errors(jsonData), key=lambda e:e.path)  
            response = []
            response.append("verilen json geçersiz") 
            for error in errors:
                response.append(error.message)
            listToM = ' & '.join([str(elt) for elt in response])    
            return listToM                
    return response       

@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        key_input = request.form['key']
        value_input = request.form['value']
        
        cursor = collection.find({ key_input : value_input})                 
        cursor_dict = [ x for x in cursor]
        cursor_json = json.dumps(cursor_dict, default=json_util.default)
        return cursor_json
    else:
        return render_template('search.html') 

@app.route('/find', methods=['POST', 'GET'])  
def find():
    if request.method == 'POST':
        id = request.form['id']
        id_int = int(id)
        cursor = collection.find({"json_body.application.id": id_int }) 
    
        cursor_dict = [ x for x in cursor]
        cursor_json = json.dumps(cursor_dict, default=json_util.default)
        return cursor_json
    else:
        return render_template('find.html')        

@app.route('/admin', methods=['POST', 'GET'])
def admin():
    if request.method == 'POST':
        id_db = int(request.form['id_db'])
        id_app = int(request.form['id_app'])
        kurulum_saati = request.form['k_saati']
        is_birimi = request.form['i_birimi']
        sunucu_ismi = request.form['s_ismi']
        sunucu_tech = request.form['s_tech']
        middleware = request.form['mid']
        direct_dbs = request.form['d_dbs']
        db_tech_client = request.form['db_tech']
        gelistirici = request.form['gelistirici']
        takim = request.form['takim']
        takim_direktor = request.form['t_direktor']
        tech = request.form['tech']
        repo = request.form['repo']
        jsonData = {
	        "_id" : id_db,
	        "json_body":{
                "application": {
                    "id" : id_app,
                    "business":  {
                        "kurulum_saati": kurulum_saati,
                        "is_birimi" : is_birimi
                    },
                    "infrastructure" : {
                        "sunucu_ismi" : sunucu_ismi,
                        "sunucu_teknoloji": sunucu_tech,
                        "middleware": middleware,
                        "direct_DBS": direct_dbs,
                        "db_Tech_Client": db_tech_client
                    },
                    "software":{
                        "gelistirici": gelistirici,
                        "takim" : takim,
                        "takim_direktoru" : takim_direktor,
                        "teknoloji" : tech,
                        "repository" : repo
                    }
                }
            }
        }
        collection.insert(jsonData)
        return redirect('/home')

  
    else:          
        return render_template('admin.html')        

# running on debug mode while development
if __name__ == '__main__':
    app.run(debug=True)
