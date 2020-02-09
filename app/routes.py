from flask import render_template, send_file, make_response, request
from app import app
from flask_bootstrap import Bootstrap
import MathPart as mp
import base64


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    # pgain = mp.stockPriceCalculator("TSLA", 1000, "2020-02-03", "2020-02-07")
    stock = 'Enter a Stock'
    if request.method == 'POST':
        stock = request.form.get('stock')
        init = request.form.get('init')
        start = request.form.get('start')
        end = request.form.get('end')
        # mp.stockPriceCalculator(stock, init, start, end)

        bytes_obj = mp.stockPlotter(stock, start, end)
        # session['stock'] = stock
        plot_url = base64.b64encode(bytes_obj.getvalue()).decode()
        return render_template(
            'index.html', title='Stock Tracker', stock=stock, plot_url=plot_url)
    return render_template(
        'index.html', title='Stock Tracker', stock=stock)
