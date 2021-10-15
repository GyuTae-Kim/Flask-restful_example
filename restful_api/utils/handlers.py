from flask import got_request_exception


def connect_exception(app):
    def log_exception(sender, exception, **extra):
        """ Log an exception to flask logging framework """
        sender.logger.debug(f'Got exception during processing: {exception}')

    got_request_exception(log_exception, app)
