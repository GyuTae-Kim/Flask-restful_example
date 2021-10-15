import numpy as np
import pandas as pd
import math

from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage


class CalculateResource(Resource):
    
    def post(self, *args, **kwargs):
        parser = reqparse.RequestParser()
        parser.add_argument('calc', type=str, required=True)
        parser.add_argument('data', type=FileStorage, location="files")
        args = parser.parse_args()
        
        df = pd.read_csv(args['data'])        
        df = df.transpose()
        df.rename(columns=df.iloc[0], inplace=True)
        df = df.drop(df.index[0])
        scores = df['score'].tolist()
        scores = list(map(int, scores))
        
        if args['calc'] == 'mean':
            res = np.mean(scores, dtype=float)
        else:
            res = np.sum(scores, dtype=float)
        
        return {'result': res}
