from flask import render_template, send_file, make_response
from app import app
from flask_bootstrap import Bootstrap
import MathPart as mp

@app.route('/')
@app.route('/index')
def index():
    pgain = mp.stockPriceCalculator("TSLA", 1000, "2020-02-03", "2020-02-07")
    return render_template('index.html', title='Stock Tracker', pgain=pgain)

@app.route('/plots/mainplot', methods=['GET'])
def mainplot():
    bytes_obj = mp.stockPlotter("TSLA", "2020-01-02", "2020-02-07")

    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')
