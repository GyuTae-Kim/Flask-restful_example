import pandas as pd

from flask_restful import Resource, reqparse, request, fields, marshal_with, marshal


calculate_fields = {
    'calc': fields.String,
    'data': fields.
}


class CalculateResource(Resource):
    
    def get(self, *args, **kwargs):
        pass
    
    def post(self, *args, **kwargs):
        pass
