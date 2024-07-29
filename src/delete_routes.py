import json
from flask import Blueprint, jsonify, request

from service.db.dbConfig import *


delete_routes = Blueprint('delete_routes', __name__)

@delete_routes.route('/delete/<int:id>', methods=['DELETE'])
def delete_data(id: int):
  response = delete_data_from_db(id)
  return jsonify(response)