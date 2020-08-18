from flask import render_template, make_response, request, redirect, url_for
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

# import MathPart as mp
from app.forms import StockForm


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = StockForm()
    if form.validate_on_submit():
        redirect(url_for('plot'))

    return render_template('index.html', form=form)

@app.route('/plot')
def plot():
    fig = px.line(x=["a","b","c"], y=[1,3,2], title="sample figure")

    figdiv = to_html(fig, full_html=False, include_plotlyjs=False)

    return render_template('plot.html', figdiv=figdiv)
