class Config(object):
    DEBUG = False
    TESTING = False
    MONGO = {
        'DATABASE': 'ezblog',
        'HOST': 'localhost',
        'PORT': 27017
    }
    PORT = 5000
    SECRET_KEY = 'qwerty'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
