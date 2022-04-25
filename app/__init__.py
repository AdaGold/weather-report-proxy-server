from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    from .routes import proxy_bp
    app.register_blueprint(proxy_bp)

    return app
