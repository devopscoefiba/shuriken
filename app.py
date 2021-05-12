from flask import Flask, redirect, render_template, request
from flask_mongoengine import MongoEngine
from models.post import Post
from utils import *
import templates, settings
from schema import * 
from logging import raiseExceptions
from os import error

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
        
        #jsonData = json.loads(' '.join([str(elt) for elt in t]))
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


# running on debug mode while development
if __name__ == '__main__':
    app.run(debug=True)
