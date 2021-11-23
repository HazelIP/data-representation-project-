# This is the server
#!flask/bin/python

from flask import Flask, jsonify,  request, abort, make_response

app = Flask(__name__,
            static_url_path='', 
            static_folder='../')

# get all
@app.route('/')
def index():
    return "Hello!"

# CRUD
@app.route('/one')
def get_all():
    return "served by get all()"

@app.route('/one/<int:id>')
def get_by_id():
    return "served by get by id"















if __name__ == '__main__' :
    app.run(debug= True)   