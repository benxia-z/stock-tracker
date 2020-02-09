from flask import render_template, send_file, make_response, request, redirect, url_for
from app import app
from flask_bootstrap import Bootstrap
import MathPart as mp
import base64


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    # pgain = mp.stockPriceCalculator("TSLA", 1000, "2020-02-03", "2020-02-07")
    stock = ''
    submitted = False
    error = None
    error1 = None
    if request.method == 'POST':
        stock = request.form.get('stock')
        init = request.form.get('init')
        start = request.form.get('start')
        end = request.form.get('end')
        submitted = request.form.get('submitted')
        if stock == None:
            stock = ''
            return render_template('index.html')
        if not mp.isStockReal(stock):
            error = True
            return render_template('index.html', error=error)
        if submitted == 'Try Again?':
            return redirect(url_for('index'))
        answers = mp.stockPriceCalculator(stock, round(float(init), 2), start, end)
        if answers == False:
            error1 = True
            return render_template('index.html', error1=error1)
        bytes_obj = mp.stockPlotter(stock, start, end)
        submitted = True
        # session['stock'] = stock
        plot_url = base64.b64encode(bytes_obj.getvalue()).decode()
        return render_template(
            'index.html', stock=stock, plot_url=plot_url, submitted=submitted, answers=answers)
    return render_template(
        'index.html', stock=stock, submitted=submitted)
