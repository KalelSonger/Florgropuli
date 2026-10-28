from flask import Flask
from dotenv import load_dotenv
import os

env_path = os.path.join(os.path.dirname(__file__), "passwords.env")
load_dotenv(env_path)


def create_app():
    app = Flask(
        __name__,
        template_folder="frontend/templates",
        static_folder="frontend/static",
    )
    app.secret_key = os.environ["SECRET_KEY"]

    from .backend.routes import routes  # backend file for page routing

    app.register_blueprint(routes, url_prefix="/")

    return app
