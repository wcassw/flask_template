from urllib.parse import quote
from sqlalchemy.engine import create_engine

class BaseConfig(object):
    TESTING = False
    UPLOAD_FOLDER = 'static/uploads'  # changed to relative path
    TEMPLATE = 'static/template'  # changed to relative path
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    VERSION = ''
    DBNAME = 'template.db'
    SECRET_KEY = "you-will-never-guess"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLAlCHEMY_ECHO = False
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    # DB
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{CREDS}@localhost:3306/{BaseConfig.DBNAME}'.format(quote('s!ldfans'), DBNAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(BaseConfig.DBNAME)
    DEBUG = True


class TestingConfig(BaseConfig):
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:%s@localhost:3306/{BaseConfig.DBNAME}' % quote('s!ldfans')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}.test'.format(BaseConfig.DBNAME)
    TESTING = True
    WTF_CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:%s@localhost:3306/{BaseConfig.DBNAME}' % quote('s!ldfans')
    DEBUG = False


config_setting = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
