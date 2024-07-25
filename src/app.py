# py -m flask --app tapp run
import json
from service.helper import *
from service.db.dbConfig import *
from flask import Flask, jsonify, request

app = Flask(__name__)   


next_management_id=14

@app.route('/all', methods=['GET'])
def get_all_fucking_data():
  my_data = get_all_data()
  return jsonify(my_data)

@app.route('/users', methods=['POST'])
def create_user():
  global next_management_id
  input_data = json.loads(request.data)
  if not (input_data):
    return jsonify({ 'error': 'Invalid user properties.' }), 400
  input_data['study_management_id'] = next_management_id
  insert_data_response = insert_data(next_management_id, input_data)
  
  next_management_id += 1
  
  return insert_data_response


""""
Get Method are from here
Getby data by types, send the datatypes and retrieve data
get data by id, send the datatypes and id , if they match then retrieve dat
"""

@app.route('/test', methods=['GET'])
def get_data():
  my_data = insert_data(1, {'mgr_id':103,'mgr_name':'John'})
  return jsonify(my_data)

@app.route('/departments', methods=['GET'])
def get_departments():
  result = jsonify(get_data_by_type("departments"))
  return result

@app.route('/departments/<int:id>', methods=['GET'])
def get_department_by_id(id: int):
  department = get_data_by_route_id("departments",id, "dept_id")
  if department is None:
    return jsonify({ 'error': 'department does not exist'}), 404
  return jsonify(department)

@app.route('/exams', methods=['GET'])
def get_exams():
  result = jsonify(get_data_by_type("exams"))
  return (result)

@app.route('/exams/<int:id>', methods=['GET'])
def get_exam_by_id(id: int):
  exam = get_data_by_route_id("exams",id, "exam_id")
  if exam is None:
    return jsonify({ 'error': 'exams does not exist'}), 404
  return jsonify(exam)

@app.route('/managers',methods=['GET'])
def get_managers():
  result = jsonify(get_data_by_type("managers"))
  return (result)

@app.route('/managers/<int:id>',methods=['GET'])
def get_manager_by_id(id:int):
  manager = get_data_by_route_id("managers", id, "mgr_id")
  if manager is None:
    return jsonify({'error':'manager does not exits'}), 404
  return jsonify(manager)

@app.route('/studies',methods=['GET'])
def get_study():
  result = jsonify(get_data_by_type("studies"))
  return (result)

@app.route('/studies/<int:id>',methods=['GET'])
def get_study_by_id(id:int):
  std = get_data_by_route_id("studies",id, "study_id")
  if std is None:
    return jsonify({'error':'Study does no exits'}), 404
  return jsonify(std)

if __name__ == '__main__':
  #app.run(debug=true)
  app.run(port=5000,debug=True)