from flask import Flask, redirect, render_template, request
from flask_mongoengine import MongoEngine
from models.post import Post
from utils import *
import templates, settings

# define flask as app
app = Flask(__name__)


# Redirect lost people to home :)
@app.route('/')
def go_home():
    return redirect('/home')

# Search Data Page
@app.route('/search')
def searchData():
    return render_template('search.html')

# Add Data Page
@app.route('/add')
def addData():
    return render_template('add.html')

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


# running on debug mode while development
if __name__ == '__main__':
    app.run(debug=True)
