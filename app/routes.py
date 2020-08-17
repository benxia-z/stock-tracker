from flask import render_template, make_response, request, redirect, url_for
from app import app
from flask_bootstrap import Bootstrap
import base64

# import MathPart as mp
from app.forms import StockForm


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = StockForm()
    if form.validate_on_submit():
        stock = form.stock.data
        init_invest = form.init_invest.data
        start_date = form.start_date.data
        end_date = form.end_date.data

        redirect(url_for('index'))

    return render_template('index.html', form=form, user='Arjun')

@app.route('/plot')
def plot():
    return render_template()
