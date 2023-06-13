from flask import Flask


def create_app(test_config: map = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    from . import main_controller
    app.register_blueprint(main_controller.bp)
    app.add_url_rule('/', endpoint='index')

    return app
