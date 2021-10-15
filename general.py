import os
import json
import yaml

from flask.helpers import make_response


def mkdir(path):
    if os.path.exists(path):
        if not os.isdir(os.path.exists):
            os.mkdir(path)
    else:
        os.mkdir(path)

def load_yaml(path):
    with open(path, 'r') as f:
        res = yaml.load(f, Loader=yaml.FullLoader)
    
    return res

def output_json(data, code, headers=None):
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    
    return resp
