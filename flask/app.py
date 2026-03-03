"""
# TODO Sharvesh 
# TODO Jishnu
"""

from __future__ import annotations

import os
from flask import Flask

from flask.auth_routes import auth_bp
from flask.room_routes import room_bp
from flask.match_routes import match_bp
from flask.game_mode_routes import game_mode_bp
from flask.voting_routes import voting_bp
from flask.analytics_routes import analytics_bp

def create_app() -> Flask:
    """
    Create and configure the Flask application.

    Returns
    -------
    Flask
        Fully configured application instance.
    """
    app = Flask(__name__)

    # TODO Sharvesh
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "change-me-in-production")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL", "sqlite:///chameleon.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # TODO Sharvesh — uncomment once db.py is complete:
    # from backend.db import init_db
    # init_db(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(room_bp)
    app.register_blueprint(match_bp)
    app.register_blueprint(game_mode_bp)
    app.register_blueprint(voting_bp)
    app.register_blueprint(analytics_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    # TODO ALL — switch debug=False and host="0.0.0.0" after Testing Phase
    app.run(debug=True, host="127.0.0.1", port=5000)
