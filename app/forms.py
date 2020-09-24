from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class StockForm(FlaskForm):
    start_date = DateField('Start Date', validators=[DataRequired()])
    end_date = DateField('End Date', validators=[DataRequired()])
    
    stock_name1 = StringField('Stock 1', validators=[DataRequired()])
    init_invest1 = DecimalField('Initial Investment', validators=[DataRequired()])
    recurring_invest1 = DecimalField('Recurring Investment Amount', validators=[DataRequired()])
    frequency_of_recurring_invest1 = SelectField("Frequency of Recurring Investments", 
        choices=[("none", "None"),("monthly", "Monthly"), ("quarterly", "Quarterly"), 
                 ("biyearly", "Biyearly"), ("yearly", "Yearly")], validators=[DataRequired()])

    stock_name2 = StringField('Stock 2', validators=[])
    init_invest2 = DecimalField('Initial Investment', validators=[])
    recurring_invest2 = DecimalField('Recurring Investment Amount', validators=[])
    frequency_of_recurring_invest2 = SelectField("Frequency of Recurring Investments", 
        choices=[("none", "None"),("monthly", "Monthly"), ("quarterly", "Quarterly"), 
                 ("biyearly", "Biyearly"), ("yearly", "Yearly")], validators=[])

    stock_name3 = StringField('Stock 3', validators=[])
    init_invest3 = DecimalField('Initial Investment', validators=[])
    recurring_invest3 = DecimalField('Recurring Investment Amount', validators=[])
    frequency_of_recurring_invest3 = SelectField("Frequency of Recurring Investments", 
        choices=[("none", "None"),("monthly", "Monthly"), ("quarterly", "Quarterly"), 
                 ("biyearly", "Biyearly"), ("yearly", "Yearly")], validators=[])

    submit = SubmitField('Submit')
    