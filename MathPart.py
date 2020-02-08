import yfinance as yf

def stockPriceCalculator(name, initAmount, startDate, endDate):
    numOfStocks = 0
    initInvestment = 0.00
    initStockPrice = 0.00
    endStockPrice = 0.00
    endValueOfInvestment = 0.00
    investmentGain = 0.00


    initStockPrice = stockPriceLocator(name, startDate)
    endStockPrice = stockPriceLocator(name, endDate)

    numOfStocks = int(initAmount/initStockPrice)
    print ("The value of the stock on " + startDate + " was $" + str(initStockPrice))
    initInvestment = numOfStocks * initStockPrice
    print("You were able to buy " + str(numOfStocks) + " stocks at $" + str(initInvestment))

    endValueOfInvestment = round((numOfStocks * endStockPrice), 2)
    print ("The value of the stock on " + endDate + " was $" + str(endStockPrice))
    print("Your investment was worth $" + str(endValueOfInvestment) + " on " + endDate)

    investmentGain = round((endValueOfInvestment - initInvestment), 2)
    print("Your investment gained $" + str(investmentGain))

def stockPriceLocator(name1, date):
    stockName = yf.Ticker(name1)
    stockPrice = 0.00

    stockDataTable = stockName.history(start = date, end = date)
    stockPrice = float(stockDataTable.loc[date, "Close"])
    return stockPrice

try:
    stockPriceCalculator("FB", 1000, "2016-05-30", "2020-02-07")
except:
    pass
