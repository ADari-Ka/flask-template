from flask import request, jsonify, make_response, Blueprint

from app import get_db_session
# from app.models import Entity


blueprint_api = Blueprint('api', __name__)


@blueprint_api.route('/relation', methods=['GET', ])
def relation():  # making responses for many-to-many relations
    args = request.args

    session = get_db_session()

    if request.method == 'GET':
        pass 

    return make_response(jsonify({'result': {'status': 'OK'}}), 200)
