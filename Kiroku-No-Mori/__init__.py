import os
from flask import Flask, render_template

# import test
# load_dotenv()
# CLIENT_ID = os.getenv("CLIENT_ID")

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/hello')
    def hello():
        return "Hello, World!"
    
    @app.route('/')
    def index():
        return render_template("index.html")

    return app