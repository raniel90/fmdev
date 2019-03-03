from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Category import CategoryResource
from resources.Comment import CommentResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes

api.add_resource(Hello, '/hello')
api.add_resource(CategoryResource, '/category')
api.add_resource(CommentResource, '/comment')