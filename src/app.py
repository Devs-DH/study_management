# py -m flask --app app run
import json
from service.helper import *
from flask import Flask, jsonify, request

app = Flask(__name__)   

#deparment information 
departments=[
  {'dept_id':101,'dept_name':'engineer'},
  {'dept_id':102,'dept_name':'Consultant'},
  {'dept_id':103,'dept_name':'Sales'}
]

exams=[
  {'exam_id':101,'exam_time':'engineer', 'exam_center':'a', 'exam_subject':'b', 'exam_plan':'c', 'exam_cost':112},
  {'exam_id':102,'exam_time':'engineer', 'exam_center':'a', 'exam_subject':'b', 'exam_plan':'c', 'exam_cost':1120},
  {'exam_id':104,'exam_time':'engineer', 'exam_center':'a', 'exam_subject':'b', 'exam_plan':'c', 'exam_cost':5112},
  {'exam_id':110,'exam_time':'engineer', 'exam_center':'a', 'exam_subject':'b', 'exam_plan':'c', 'exam_cost':1152},
  {'exam_id':105,'exam_time':'engineer', 'exam_center':'a', 'exam_subject':'b', 'exam_plan':'c', 'exam_cost':1212},
]

@app.route('/departments', methods=['GET'])
def get_departments():
  return jsonify(departments)

@app.route('/department/<int:id>', methods=['GET'])
def get_department_by_id(id: int):
  department = get_data_from_id(id, "dept_id", departments)
  if department is None:
    return jsonify({ 'error': 'department does not exist'}), 404
  return jsonify(department)

@app.route('/exams', methods=['GET'])
def get_exams():
  return jsonify(exams)


@app.route('/exams/<int:id>', methods=['GET'])
def get_exam_by_id(id: int):
  exam = get_data_from_id(id, "exam_id", exams)
  if exam is None:
    return jsonify({ 'error': 'exams does not exist'}), 404
  return jsonify(exam)
"""
Manager get class start form here -Dipesh
"""
managers=[
  {'mgr_id':101,'mgr_name':'Imi'},
  {'mgr_id':102,'mgr_name':'comsom'},
  {'mgr_id':103,'mgr_name':'John'}
  ]

@app.route('/manager',methods=['GET'])
def get_managers():
  return jsonify(managers)

@app.route('/manager/<int:id>',methods=['GET'])
def get_manager_by_id(id:int):
  manager = get_data_from_id(id,"mgr_id",managers)
  if manager is None:
    return jsonify({'error':'manager does not exits'}), 404
  return jsonify(manager)

if __name__ == '__main__':
  #app.run(debug=true)
  app.run(port=5000)
  app.run(debug = True)
