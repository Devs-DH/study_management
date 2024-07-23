# py -m flask --app app run
import json
from service.departmentService import *
from service.managerService import *
from flask import Flask, jsonify, request

app = Flask(__name__)   

#deparment information 
departments=[
  {'dept_id':101,'dept_name':'engineer'},
  {'dept_id':102,'dept_name':'Consultant'},
  {'dept_id':103,'dept_name':'Sales'}
]

@app.route('/department', methods=['GET'])
def get_departments():
  return jsonify(departments)

@app.route('/department/<int:id>', methods=['GET'])
def get_department_by_id(id: int):
  department = get_department(id, departments)
  if department is None:
    return jsonify({ 'error': 'department does not exist'}), 404
  return jsonify(department)

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
  manager = get_manager(id,managers)
  if manager is None:
    return jsonify({'error':'manager does not exits'}), 404
  return jsonify(manager)

if __name__ == '__main__':
  #app.run(debug=true)
  app.run(port=5000)
  app.run(debug = True)
