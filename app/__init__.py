from flask import Flask


def create_app(config=None):
    app = Flask(__name__)
    
    return app


def bootstrap_app(app=None, config=None):
    if not app:
        app = create_app(config)
    elif config:
        app.config.update(config)
    
    return app
