my_db = [
  {"study_management_id": 1, "type_key": "departments", 'dept_id':101, 'dept_name':'engineer'},
  {"study_management_id": 2, "type_key": "departments", 'dept_id':102,'dept_name':'Consultant'},
]

def get_data_from_db(id: int):
  return next((d for d in my_db if d["study_management_id"] == id), None)

def insert_data(id, data):
  same_id = next((d for d in my_db if d["study_management_id"] == id), None)
  
  if same_id is None:
    my_db.append(data)
    return {"success": "true", "data": data }
  return {"success": "false", "data": {"error": "error"} }