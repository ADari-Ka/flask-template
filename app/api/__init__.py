from flask_restful import Api

from .relations import blueprint_api

api = Api(blueprint_api)

from .resources import entity

# api.add_resource(entity.EntityResource, '/entity/<TYPE:PARAMETER>', subdomain='api')
