from flask import Flask


def create_app(config=None):
    app = Flask(__name__)

    app.config.from_pyfile('default_settings.cfg')

    if config:
        app.config.from_object(config)
    
    return app


def bootstrap_app(app=None, config=None):
    if not app:
        app = create_app(config)
    elif config:
        app.config.update(config)
    
    return app
