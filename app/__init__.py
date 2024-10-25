from flask import Flask
from flask_cors import CORS
from .routes import bp as proxy_bp

def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    app.register_blueprint(proxy_bp)

    return app
