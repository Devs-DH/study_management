import json 
from flask import Flask, Blueprint, jsonify, request

from service.db.dbConfig import *


post_routes = Blueprint('post_routes', __name__)

next_management_id=19

@post_routes.route('/all', methods=['GET'])
def get_all_fucking_data():
  my_data = get_all_data()
  return jsonify(my_data)

@post_routes.route('/users/create', methods=['POST'])
def create_user():
  global next_management_id
  input_data = json.loads(request.data)
  if not (input_data):
    return jsonify({ 'error': 'Invalid user properties.' }), 400
  input_data['study_management_id'] = next_management_id
  insert_data_response = insert_data(next_management_id, input_data)
  
  next_management_id += 1
  
  return insert_data_response


@post_routes.route('/login/users', methods=['POST'])
def login_user():
  try:
    input_data = json.loads(request.data)
    if not (input_data):
      return jsonify({ 'error': 'Invalid body.' }), 400
  
    user_data = get_data_by_route_id("users", input_data["user_id"], "user_id")
    if not (input_data["password"] == user_data[0]["password"] and not(user_data[0]["role"] == "manager")):
      return jsonify({ 'error': 'Invalid id or password.' }), 400
    return jsonify({'status': 'success', 'message': 'Nice'})
  except:
    return jsonify({ 'error': 'Internal Server Error' }), 500
  
#manager login  
@post_routes.route('/login/managers',methods=['POST'])
def login_manger():
    try:
      input_data = json.loads(request.data)
      if not (input_data):
        return json({'error':'Invalid body.'}),400
      
      user_data = get_data_by_route_id("users",input_data["user_id"],"user_id")
      if not (user_data[0]["password"] == input_data["password"]  and user_data[0]["role"] == "manager"):
        return jsonify({'error':'Invalid id or password'}),400
      return jsonify({'status':'sucess','message':'nice'})
    except:
        return jsonify({'error':'Internal Server Error'}),500
      
#exam
@post_routes.route('/insert',methods=['POST'])
def create_new_data():
    try:
      global next_management_id
      input_data = json.loads(request.data)
      if not (input_data):
        return jsonify({ 'error': 'Invalid user properties.' }), 400
      input_data['study_management_id'] = next_management_id
      insert_data_response = insert_data(next_management_id, input_data)
      next_management_id += 1
      return insert_data_response
    except:
        return jsonify({'error':'Internal Server Error'}),500
    