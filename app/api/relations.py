from flask import request, jsonify, make_response, Blueprint

from app import get_db_session
from app.models import Entity


blueprint_relations = Blueprint('relations', __name__, template_folder='')


@blueprint_relations.route('/api/relation', methods=['POST', ])
def relation():  # making responses for many-to-many relations
    args = request.args

    session = get_db_session()
    entity = session.query(Entity).filter().first()

    if request.method == 'POST':
        pass 

    session.commit()

    return make_response(jsonify({'result': {'status': 'OK'}}), 200)
