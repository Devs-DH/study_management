import json 
from flask import Blueprint, jsonify, request

from service.db.dbConfig import * 


put_routes = Blueprint('put_routes', __name__)


@put_routes.route('/update', methods=['PUT'])
def update():
    try:
        input_data = json.loads(request.data)
        if not (input_data):
            return jsonify({'error':'Invalid body.'}),400
        
        result = update_data(input_data)

        if result.get('Update success') == "True":
            return jsonify(result),200
        else:
            return jsonify(result),400
        
    except:
        return jsonify({'error':'Internal Server Error'}),500