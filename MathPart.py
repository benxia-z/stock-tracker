import yfinance as yf
def stockPriceCalculator(name, initInvestment, investmentDate, currentDate):

    initStockPrice = 0.00
    numOfStocks = 0
    currentStockPrice = 100.0
    currentValueOfInvestment = 0.0

    numOfStocks = (int)(initInvestment/initStockPrice)

    currentValueOfInvestment = numOfStocks * currentStockPrice

    return currentValueOfInvestment



appleStock = yf.Ticker("AAPL")

appleStock.info
