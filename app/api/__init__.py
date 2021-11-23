from flask_restful import Api

from .relations import blueprint_api

api = Api(blueprint_api)

from .resources import *

# api.add_resource(EntityResource, '/entity/<TYPE:PARAM>', subdomain='api')
# api.add_resource(EntitiesResource, '/entitities', subdomain='api')
