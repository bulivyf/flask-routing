from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from flask_moment import Moment
# from flask_debugtoolbar import DebugToolbarExtension

from .config import config_by_name

# db = SQLAlchemy()

# Configure authentication
# login_manager = LoginManager()
# login_manager.session_protection = "strong"
# login_manager.login_view = "auth.login"

# toolbar = DebugToolbarExtension()

# moment = Moment()


def create_app(config_name):
    file_settings = '__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__, __name__, str(__package__))

    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    # db.init_app(app)
    # login_manager.init_app(app)
    # moment.init_app(app)
    # toolbar.init_app(app)
    # print(file_settings)

    from .views.main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    return app


print( str(__package__)+" init done")
