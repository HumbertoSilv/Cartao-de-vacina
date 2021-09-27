from flask import Flask
from app.configs import database, migrate, env_configs
from app.routes import vaccination_bp


def create_app():
    app = Flask(__name__)

    env_configs.init_app(app)
    database.init_app(app)
    migrate.init_app(app)

    app.register_blueprint(vaccination_bp.bp)

    return app
