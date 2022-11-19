import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    CSRF_ENABLE = bool(os.getenv("CSRF_ENABLE"))


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = bool(os.getenv("DEBUG"))


class TestingConfig(Config):
    TESTING = bool(os.getenv("DEBUG"))


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig
}
