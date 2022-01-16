from flask import jsonify, make_response
from flask_restful import Resource, reqparse

from app import get_db_session
from app.models import Entity


class EntityResource(Resource):
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('title', required=True)
    # needed fields

    put_parser = reqparse.RequestParser()  # the same thing, but for put response 

    def get(self, param):
        session = get_db_session()
        
        '''
        entity = session.query(Entity).filter(param).first()

        return make_response(jsonify({'result': {'entity': 
                             entity.to_dict(only=('id', 'title', 'FIELDS', 
                                                  'additional.FIELD'))}}), 200)

        '''

    def delete(self, param):
        session = get_db_session()
        
        '''
        '''
        # session.delete(entity)
        session.commit()

        return make_response(jsonify({'result': {'success': 'OK'}}), 200)
    
    def post(self, param):

        args = EntityResource.post_parser.parse_args()  # to get use fields use args['FIELD']

        '''
        '''

        session = get_db_session()
        entity = Entity()
        entity.title = args['title']

        session.add(entity)
        session.commit()

        return make_response(jsonify({'result': {'success': 'OK'}}), 201)
    
    def put(self, param):
        session = get_db_session()
        entity = session.query(Entity).filter(param).first()

        '''
        '''

        args = EntityResource.put_parser.parse_args()

        for key, value in args.items():
            '''
            '''
            entity.__setattr__(key, value)

        session.commit()

        return make_response(jsonify({'result': {'success': 'OK'}}), 200)


class EntitiesResource(Resource):
    '''
    I also prefer to create API for entities in the plural
    Logic the same (parsers, work with db, etc)
    '''
    pass
