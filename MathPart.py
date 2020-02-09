import yfinance as yf
import matplotlib.pyplot as plt

from datetime import datetime

def stockPriceCalculator(name, initAmount, startDate, endDate):
    numOfStocks = 0
    initInvestment = 0.00
    initStockPrice = 0.00
    endStockPrice = 0.00
    endValueOfInvestment = 0.00
    investmentGain = 0.00
    percentageGain = 0.00


    initStockPrice = stockPriceLocator(name, startDate)
    endStockPrice = stockPriceLocator(name, endDate)

    numOfStocks = int(initAmount/initStockPrice)
    startInfo = "The value of the stock on " + startDate + " was $" + str(initStockPrice)
    initInvestment = numOfStocks * initStockPrice
    buyInfo = "You were able to buy " + str(numOfStocks) + " stocks at $" + str(initInvestment)

    endValueOfInvestment = round((numOfStocks * endStockPrice), 2)
    endStockInfo = "The value of the stock on " + endDate + " was $" + str(endStockPrice)
    endInvestmentInfo = "Your investment was worth $" + str(endValueOfInvestment) + " on " + endDate

    investmentGain = round((endValueOfInvestment - initInvestment), 2)
    investmentGainInfo = "Your investment gained $" + str(investmentGain)

    percentageGain = round(((endValueOfInvestment - initInvestment)/initInvestment) * 100, 2)
    percentageGaininfo = "That's a " + str(percentageGain) + "% gain!"

    returnInfo = startInfo + '\n' + buyInfo + '\n' + endStockInfo + '\n' + endInvestmentInfo + '\n' + investmentGainInfo + '\n' + percentageGaininfo + '\n'

    return (returnInfo)

def stockPriceLocator(name1, date):
    stockName = yf.Ticker(name1)
    stockPrice = 0.00

    stockDataTable = stockName.history(start = date, end = date)
    print (stockDataTable)
    stockPrice = float(stockDataTable.loc[date, "Close"])
    return stockPrice

def stockPlotter(name2, startDate2, endDate2):
    stockName = yf.Ticker(name2)
    dateList = []
    priceList = []
    xTicks = []
    yTicks = []
    dateListSize = 0
    stockDataTable = stockName.history(start = startDate2, end = endDate2)

    for row in stockDataTable.itertuples():
        dateString = row.Index.strftime("%Y-%m-%d")
        dateList.append(dateString)
        priceList.append(row.Close)

    dateListSize = len(dateList)

    if(dateListSize < 15):
        xTicks = dateList
        yTicks = priceList
    elif(dateListSize < 45):
        for i in range(0, dateListSize, 3):
            xTicks.append(dateList[i])
            yTicks.append(priceList[i])

    print (xTicks)
    print (yTicks)

    plt.plot(xTicks, yTicks)
    plt.title(name2 + " Performance", fontsize = 20)
    plt.xlabel('Date', fontsize = 14)
    plt.xticks(rotation = 60)
    plt.ylabel('Price ($)', fontsize = 14)
    plt.show()

print(stockPriceCalculator("TSLA", 1000, "2020-01-02", "2020-02-07"))
stockPlotter("TSLA", "2020-01-02", "2020-02-07")
