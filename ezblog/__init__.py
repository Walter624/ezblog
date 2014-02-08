__version__ = '0.1'
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
app = Flask('ezblog')
app.config['SECRET_KEY'] = 'qwerty'
app.debug = True
toolbar = DebugToolbarExtension(app)
from ezblog.controllers import *