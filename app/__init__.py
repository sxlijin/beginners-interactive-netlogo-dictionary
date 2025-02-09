from flask import Flask
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome

app = Flask(__name__)
fa = FontAwesome(app)
app.config['TEMPLATES_AUTO_RELOAD'] = True

from app import routes