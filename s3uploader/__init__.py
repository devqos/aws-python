import flask


def create_app(test_config=None) -> flask.Flask:
    app = flask.Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    register_blueprints(app)

    return app


def register_blueprints(app: flask.Flask) -> None:
    from s3uploader.controllers import main_controller
    app.register_blueprint(main_controller.bp)
    app.add_url_rule('/', endpoint='index')
