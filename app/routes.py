from flask import render_template
from app import app
from flask_bootstrap import Bootstrap
import MathPart as mp

@app.route('/')
@app.route('/index')
def index():
    pgain = mp.stockPriceCalculator("TSLA", 1000, "2020-02-03", "2020-02-07")
    return render_template('index.html', title='Stock Tracker', pgain=pgain)
