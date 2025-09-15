from flask import Flask
from src.controllers import IndexController
from src.routes import set_routes

def create_app():
    app = Flask(__name__)

    # Set up middleware and configurations here if needed

    set_routes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)