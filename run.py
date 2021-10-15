from flask import Flask
from flask_restful import Resource
import flask_restful

from general import mkdir
from restful_api.utils.errors import errors

def init_mkdir(settings):
    hist_dir = settings['history_dir']
    log_dir = settings['log_dir']
    mkdir(hist_dir)
    mkdir(log_dir)

app = Flask(__name__)
api = flask_restful.API(app, errors=errors)


