def get_data_from_id(id: int, id_string: str, departments: list):
  return next((d for d in departments if d[id_string] == id), None)