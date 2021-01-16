from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import random
import json

app = Flask(__name__)
CORS(app)


users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

def randomID():
   id = ''
   lowercase = 'abcdefghijklmnopqrstuvwxyz'
   nums = '1234567890'
   for x in range(0,3):
      id+=random.choice(lowercase)
   for x in range(0,3):
      id+=random.choice(nums)
   return id
   
@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username or search_job:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if search_username and user['name'] == search_username:
               subdict['users_list'].append(user)
            if search_job and user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd['id'] = randomID()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      resp.status_code = 201
      resp.data = json.dumps(userToAdd)
      return resp

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
   if request.method == 'GET':
      if id :
         for user in users['users_list']:
           if user['id'] == id:
              return user
         return ({})
      return users
   elif request.method == 'DELETE':
      userToDelete = {}
      for user in users['users_list']:
         if(user['id']) == id:
            userToDelete = user
      if(userToDelete == {}):
         resp = jsonify(success=True)
         resp.status_code = 404
         return resp
      users['users_list'].remove(userToDelete)
      resp = jsonify(success=True)
      resp.status_code = 204
      return resp



