__version__ = '0.1'
import os
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

environment = os.environ.get('FLASK_ENV')
config_class = 'ProductionConfig'
if environment == 'dev':
    config_class = 'DevelopmentConfig'

app = Flask('ezblog')
app.config.from_object('ezblog.config.{0}'.format(config_class))

if app.config['DEBUG']:
    toolbar = DebugToolbarExtension(app)

from ezblog.controllers import *