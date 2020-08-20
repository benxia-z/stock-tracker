from flask import render_template, make_response, request, redirect, url_for, flash, session
from app import app
from flask_bootstrap import Bootstrap
import base64
import json
# import plotly.plotly as py
from plotly import graph_objs as go
from plotly.io import to_html
import plotly
import plotly.express as px

import numpy as np

import MathPart as mp
from app.forms import StockForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = StockForm()
    if form.validate_on_submit():
        if not mp.check_valid_stock(form.stock_name.data):
            flash('test')
            return redirect(url_for('index'))
        session['stock_name'] = form.stock_name.data
        session['init_invest'] = str(form.init_invest.data)
        session['start_date'] = str(form.start_date.data)
        session['end_date'] = str(form.end_date.data)
        session['recurring_invest'] = str(form.recurring_invest.data)
        session['frequency_of_recurring_invest'] = form.frequency_of_recurring_invest.data
        return redirect(url_for('plot'))

    return render_template('index.html', form=form)

@app.route('/plot', methods=['GET', 'POST'])
def plot():
    stock_name=session.get('stock_name'),
    init_invest=session.get('init_invest'),
    start_date=session.get('start_date'),
    end_date=session.get('end_date'),
    recurring_invest=session.get('recurring_invest'),
    frequency_of_recurring_invest=session.get('frequency_of_recurring_invest')
    
    stock_object = mp.Stock(stock_name[0], float(init_invest[0]), start_date[0], end_date[0], float(recurring_invest[0]), 
        frequency_of_recurring_invest)
    
    fig1 = stock_object.graph_stock_prices()
    fig2 = stock_object.graph_bases_vs_value()

    figdiv1 = to_html(fig1, full_html=False, include_plotlyjs=False)
    figdiv2 = to_html(fig2, full_html=False, include_plotlyjs=False)

    return render_template('plot.html',figdiv1=figdiv1, figdiv2=figdiv2)
