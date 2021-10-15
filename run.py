####################################################################################
# Reference
# https://flask-restful.readthedocs.io/en/latest/extending.html
# https://bswen.com/2021/03/others-how-to-upload-file-using-flask-restful-api.html
# https://github.com/tomasrasymas/flask-restful-api-template
####################################################################################

import argparse

from flask import Flask
import flask_restful

from general import mkdir, load_yaml
from restful_api.api_views import add_views
from restful_api.utils.errors import errors
from restful_api.utils.handlers import connect_exception

# functions
def init_mkdir(environment):
    mkdir(environment['settings']['history_dir'])
    mkdir(environment['settings']['log_dir'])

# load Flask app & api
app = Flask(__name__)
api = flask_restful.Api(app, errors=errors)

# set app & api
add_views(api)
connect_exception(app)

# main
if __name__ == '__main__':
    # argument
    parser = argparse.ArgumentParser()
    parser.add_argument('--environment', type=str, default='settings/environment.yaml', help='enter the environment file path')
    opt, _ = parser.parse_known_args()
    
    # set environment
    environment = load_yaml(opt.environment)
    init_mkdir(environment)
    
    # run
    app.run(host=environment['server']['host'],
            port=environment['server']['port'],
            debug=True)
