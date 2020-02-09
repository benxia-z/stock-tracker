from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
Bootstrap(app)
from app import routes
