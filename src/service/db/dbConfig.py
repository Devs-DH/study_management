my_db = [
  #department
  {"study_management_id": 1, "type_key": "departments", 'dept_id':101, 'dept_name':'engineer'},
  {"study_management_id": 2, "type_key": "departments", 'dept_id':102,'dept_name':'Consultant'},
  #exams

  {"study_management_id": 3, "type_key": "exams", 'exam_id':101, 'exam_time':'engineer','exam_center':"a","exam_subject":"b","exam_plan":"c","exam_cost":1203},
  {"study_management_id": 4, "type_key": "exams", 'exam_id':102, 'exam_time':'engineer','exam_center':"a","exam_subject":"b","exam_plan":"c","exam_cost":1203},
  {"study_management_id": 5, "type_key": "exams", 'exam_id':103, 'exam_time':'engineer','exam_center':"a","exam_subject":"b","exam_plan":"c","exam_cost":1203},
  {"study_management_id": 6, "type_key": "exams", 'exam_id':104, 'exam_time':'engineer','exam_center':"a","exam_subject":"b","exam_plan":"c","exam_cost":1203},
  #manager

  {"study_management_id": 7, "type_key": "managers", 'mgr_id':101, 'mgr_name':'Fabio'},
  {"study_management_id": 8, "type_key": "managers", 'mgr_id':102, 'mgr_name':'Fabio'},
  {"study_management_id": 9, "type_key": "managers", 'mgr_id':103, 'mgr_name':'Fabio'},
  {"study_management_id": 10, "type_key": "managers", 'mgr_id':104, 'mgr_name':'Fabio'},
  #study

  {"study_management_id": 11, "type_key": "studies", 'study_id':101, 'study_topic':'engineer',"context":"abc","category":"a","prerequisite":"python","cost":2102,"level":"easy","plan":"july9"},
  {"study_management_id": 12, "type_key": "studies", 'study_id':102, 'study_topic':'engineer',"context":"abc","category":"a","prerequisite":"python","cost":2102,"level":"easy","plan":"july9"},
  {"study_management_id": 13, "type_key": "studies", 'study_id':103, 'study_topic':'engineer',"context":"abc","category":"a","prerequisite":"python","cost":2102,"level":"easy","plan":"july9"},
  {"study_management_id": 14, "type_key": "studies", 'study_id':104, 'study_topic':'engineer',"context":"abc","category":"a","prerequisite":"python","cost":2102,"level":"easy","plan":"july9"},
 
  #user Login Information
  {"study_management_id": 15, "type_key": "users", 'user_id':10101, 'password':'123456','role': 'user'},
  {"study_management_id": 16, "type_key": "users", 'user_id':10102,'password':'7891011','role': 'user'},

  #manager Login Information
  {"study_management_id": 17, "type_key": "users", 'user_id':10201, 'password':'123456', 'role': 'manager', 'mgr_id':101},
  {"study_management_id": 18, "type_key": "users", 'user_id':10202,'password':'7891011','role': 'manager', 'mgr_id':102}
]


def get_all_data():
  return my_db

def get_data_from_db(id: int):
  return next((d for d in my_db if d["study_management_id"] == id), None)

#get dabase data 
def get_data_by_type(type:str):
  result = list(filter(lambda obj: (obj["type_key"]  == type), my_db))
  return result

#get database data by id
def get_data_by_route_id(type:str, id:int, id_string:str,):
  result = list(filter(lambda obj: (obj["type_key"]  == type and obj[id_string] == id), my_db))
  return result
  # return next((d for d in my_db if d[id_string] == id and d["type_key"] == type), None)


def insert_data(id:int, data:any):
  same_id = next((d for d in my_db if d["study_management_id"] == id), None)
  
  if same_id is None:
    my_db.append(data)
    return {"success": "true", "data": data }
  return {"success": "false", "data": {"error": "error"} }

def update_data(data:any):
  key = data.get("study_management_id")
  for item in my_db:
    if item['study_management_id'] == key:
      item.update(data)
      return {'Update success':"True","data":data}
    
  return {'Update Failed':"false","data":{"error":"error"}}
        