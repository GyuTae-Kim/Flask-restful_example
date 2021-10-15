from flask import got_request_exception

def log_exception(sender, exception, **extra):
    """ Log an exception to flask logging framework """
    sender.logger.debug(f'Got exception during processing: {exception}')

def connect_exception(app):
    got_request_exception.connect(log_exception, app)
