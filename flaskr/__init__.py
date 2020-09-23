import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Config')

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    with app.app_context():
        db.init_app(app)
        ma.init_app(app)
        migrate.init_app(app, db)

    @app.route('/')
    def hello():
        return render_template('mastertech.html')

    from . import users, clock
    app.register_blueprint(users.bp)
    app.register_blueprint(clock.bp)

    return app