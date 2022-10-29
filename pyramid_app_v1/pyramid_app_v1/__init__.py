from pyramid.config import Configurator
from .midlleware import get_session




def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        
        config.add_request_method(get_session, 'base', reify=True)
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()
    return config.make_wsgi_app()
