from flask import Flask, redirect, render_template
from flask_mongoengine import MongoEngine

# define flask as app
app = Flask(__name__)


#   redirect lost people to home :)
@app.route('/')
def go_home():
    return redirect('/home')


#   home route where the magic happens
@app.route('/home', methods=['GET'])
def home_page():
    return render_template('home.html')


#   running on debug mode while development
if __name__ == '__main__':
    app.run(debug=True)
