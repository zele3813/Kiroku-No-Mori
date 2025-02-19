import os
from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        #TODO establish local database instance
    )

    # Check if a test config is provided for testing purpose
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # @app.route('/hello')
    # def hello():
    #     return "Hello, World!"
    
    # Associate index endpoint with the index view function; landing page for every app instance
    @app.endpoint('index')
    def index():
        return render_template("index.html")
    
    from . import search

    app.register_blueprint(search.bp)
    app.add_url_rule("/", endpoint="index") 

    return app