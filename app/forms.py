from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class StockForm(FlaskForm):
    stock_name = StringField('Stock', validators=[DataRequired()])
    init_invest = DecimalField('Initial Investment', validators=[DataRequired()])
    start_date = DateField('Start Date', validators=[DataRequired()])
    end_date = DateField('End Date', validators=[DataRequired()])
    recurring_invest = DecimalField('Recurring Investment Amount', validators=[DataRequired()])
    frequency_of_recurring_invest = SelectField("Frequency of Recurring Investments", 
        choices=[("none", "None"),("monthly", "Monthly"), ("quarterly", "Quarterly"), 
                 ("biyearly", "Biyearly"), ("yearly", "Yearly")], validators=[DataRequired()])

    submit = SubmitField('Submit')
    