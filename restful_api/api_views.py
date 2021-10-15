from .calculate.resource import CalculateResource


def add_views(api):
    api.add_resource(CalculateResource, '/calc')
