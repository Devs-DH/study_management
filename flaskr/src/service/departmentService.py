def get_department(id: int, departments: list):
  return next((d for d in departments if d['dept_id'] == id), None)