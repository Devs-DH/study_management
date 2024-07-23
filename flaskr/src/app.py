# py -m flask --app app run
import json
from service.departmentService import *
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



if __name__ == '__main__':
  #app.run(debug=true)
  app.run(port=5000)
  app.run(debug = True)
