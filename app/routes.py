from flask import render_template, make_response, request, redirect, url_for, flash, session
from app import app
from flask_bootstrap import Bootstrap
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
        '''
        if not mp.check_valid_dates(form.stock_name1.data, form.start_date.data):
            flash('Invalid start date')
            return redirect(url_for('index'))
        if not mp.check_valid_dates(form.stock_name1.data, form.end_date.data):
            flash('Invalid end date')
            return redirect(url_for('index'))

        if not mp.check_valid_dates(form.stock_name2.data, form.start_date.data):
            flash('Invalid start date')
            return redirect(url_for('index'))
        if not mp.check_valid_dates(form.stock_name2.data, form.end_date.data):
            flash('Invalid end date')
            return redirect(url_for('index'))

        if not mp.check_valid_dates(form.stock_name3.data, form.start_date.data):
            flash('Invalid start date')
            return redirect(url_for('index'))
        if not mp.check_valid_dates(form.stock_name3.data, form.end_date.data):
            flash('Invalid end date')
            return redirect(url_for('index'))
        '''
        
        #stock 1 checks
        if not mp.check_valid_stock(form.stock_name1.data):
            flash('Invalid stock entered.')
            return redirect(url_for('index'))
        
        if not mp.check_valid_investment_amount(form.init_invest1.data):
            flash('Invalid initial investment amount for stock 1')
            return redirect(url_for('index'))

        if not mp.check_valid_recurring_amount(form.recurring_invest1.data):
            flash('Invalid recurring investment amount for stock 1')
            return redirect(url_for('index'))

        #stock 2 checks
        if not mp.check_valid_stock(form.stock_name2.data):
            flash('Invalid stock entered')
            return redirect(url_for('index'))
        
        if not mp.check_valid_investment_amount(form.init_invest2.data):
            flash('Invalid initial investment amount for stock 2')
            return redirect(url_for('index'))

        if not mp.check_valid_recurring_amount(form.recurring_invest2.data):
            flash('Invalid recurring investment amount for stock 2')
            return redirect(url_for('index'))

        #stock 3 checks
        if not mp.check_valid_stock(form.stock_name3.data):
            flash('Invalid stock entered.')
            return redirect(url_for('index'))
        
        if not mp.check_valid_investment_amount(form.init_invest3.data):
            flash('Invalid initial investment amount for stock 3')
            return redirect(url_for('index'))

        if not mp.check_valid_recurring_amount(form.recurring_invest3.data):
            flash('Invalid recurring investment amount for stock 3')
            return redirect(url_for('index'))

        session['start_date'] = str(form.start_date.data)
        session['end_date'] = str(form.end_date.data)

        session['stock_name1'] = form.stock_name1.data
        session['init_invest1'] = str(form.init_invest1.data)
        session['recurring_invest1'] = str(form.recurring_invest1.data)
        session['frequency_of_recurring_invest1'] = form.frequency_of_recurring_invest1.data

    
        session['stock_name2'] = form.stock_name2.data
        session['init_invest2'] = str(form.init_invest2.data)
        session['recurring_invest2'] = str(form.recurring_invest2.data)
        session['frequency_of_recurring_invest2'] = form.frequency_of_recurring_invest2.data

        session['stock_name3'] = form.stock_name3.data
        session['init_invest3'] = str(form.init_invest3.data)
        session['recurring_invest3'] = str(form.recurring_invest3.data)
        session['frequency_of_recurring_invest3'] = form.frequency_of_recurring_invest3.data

        return redirect(url_for('plot'))

    return render_template('index.html', form=form)

@app.route('/plot', methods=['GET', 'POST'])
def plot():
    
    stock_name1 = session.get('stock_name1'),
    init_invest1 = session.get('init_invest1'),
    start_date = session.get('start_date'),
    end_date = session.get('end_date'),
    recurring_invest1 = session.get('recurring_invest1'),
    frequency_of_recurring_invest1 = session.get('frequency_of_recurring_invest1')
    stock_object1 = mp.Stock(stock_name1[0], float(init_invest1[0]), start_date[0], end_date[0], float(recurring_invest1[0]), 
        frequency_of_recurring_invest1)

    stock_name2 = session.get('stock_name2'),
    init_invest2 = session.get('init_invest2'),
    recurring_invest2 = session.get('recurring_invest2'),
    frequency_of_recurring_invest2 = session.get('frequency_of_recurring_invest2')
    stock_object2 = mp.Stock(stock_name2[0], float(init_invest2[0]), start_date[0], end_date[0], float(recurring_invest2[0]), 
    frequency_of_recurring_invest2)

    stock_name3 = session.get('stock_name3'),
    init_invest3 = session.get('init_invest3'),
    recurring_invest3 = session.get('recurring_invest3'),
    frequency_of_recurring_invest3 = session.get('frequency_of_recurring_invest3')
    stock_object3 = mp.Stock(stock_name3[0], float(init_invest3[0]), start_date[0], end_date[0], float(recurring_invest3[0]), 
    frequency_of_recurring_invest3)

    portfolio_object = mp.Portfolio(stock_object1, stock_object2, stock_object3)
    
    fig1 = portfolio_object.graph_stock_price_subplot()
    fig2 = portfolio_object.graph_stock_basis_vs_value_subplot()
    fig3 = portfolio_object.graph_portfolio_basis_vs_value()

    figdiv1 = to_html(fig1, full_html=False, include_plotlyjs=False)
    figdiv2 = to_html(fig2, full_html=False, include_plotlyjs=False)
    figdiv3 = to_html(fig3, full_html=False, include_plotlyjs=False)

    return render_template('plot.html',figdiv1=figdiv1, figdiv2=figdiv2, figdiv3=figdiv3)
