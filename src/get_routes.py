import json
from flask import Blueprint, jsonify, request

from service.db.dbConfig import *


get_routes = Blueprint('get_routes', __name__)

# @get_routes.route('/test', methods=['GET'])
# def get_data():
#   my_data = insert_data(1, {'mgr_id':103,'mgr_name':'John'})
#   return jsonify(my_data)

@get_routes.route('/departments', methods=['GET'])
def get_departments():
  result = jsonify(get_data_by_type("departments"))
  return result

@get_routes.route('/departments/<int:id>', methods=['GET'])
def get_department_by_id(id: int):
  department = get_data_by_route_id("departments",id, "dept_id")
  if department is None:
    return jsonify({ 'error': 'department does not exist'}), 404
  return jsonify(department)

@get_routes.route('/exams', methods=['GET'])
def get_exams():
  result = jsonify(get_data_by_type("exams"))
  return (result)

@get_routes.route('/exams/<int:id>', methods=['GET'])
def get_exam_by_id(id: int):
  exam = get_data_by_route_id("exams",id, "exam_id")
  if exam is None:
    return jsonify({ 'error': 'exams does not exist'}), 404
  return jsonify(exam)

@get_routes.route('/managers',methods=['GET'])
def get_managers():
  result = jsonify(get_data_by_type("managers"))
  return (result)

@get_routes.route('/managers/<int:id>',methods=['GET'])
def get_manager_by_id(id:int):
  manager = get_data_by_route_id("managers", id, "mgr_id")
  if manager is None:
    return jsonify({'error':'manager does not exits'}), 404
  return jsonify(manager)

@get_routes.route('/studies',methods=['GET'])
def get_study():
  result = jsonify(get_data_by_type("studies"))
  return (result)

@get_routes.route('/studies/<int:id>',methods=['GET'])
def get_study_by_id(id:int): 
  std = get_data_by_route_id("studies",id, "study_id")
  if std is None:
    return jsonify({'error':'Study does no exits'}), 404
  return jsonify(std)