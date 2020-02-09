import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import io

from datetime import datetime
matplotlib.use('agg')
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

    if (numOfStocks == 0):
        print("You were not able to buy any stocks with your initial investment. Please enter a new amount: ")
        return False

    initInvestment = round((numOfStocks * initStockPrice), 2)
    buyInfo = "You were able to buy " + str(numOfStocks) + " stocks at $" + str(initInvestment)

    endValueOfInvestment = round((numOfStocks * endStockPrice), 2)
    endStockInfo = "The value of the stock on " + endDate + " was $" + str(endStockPrice)
    endInvestmentInfo = "The value of your investment on " + endDate + "was worth $" + str(endValueOfInvestment)

    investmentGain = round((endValueOfInvestment - initInvestment), 2)
    investmentGainInfo = "Your investment gained $" + str(investmentGain)

    percentageGain = round(((endValueOfInvestment - initInvestment)/initInvestment) * 100, 2)
    percentageGaininfo = "That's a " + str(percentageGain) + "% gain!"

    returnInfo = {'startInfo': startInfo,
                  'buyInfo': buyInfo,
                  'endStockInfo': endStockInfo,
                  'endInvestmentInfo': endInvestmentInfo,
                  'investmentGainInfo': investmentGainInfo,
                  'percentageGaininfo': percentageGaininfo}

    return (returnInfo)

def stockPriceLocator(name1, date):
    stockPrice = 0.00
    stockName = yf.Ticker(name1)
    stockDataTable = stockName.history(start = date)
    stockPrice = float(stockDataTable["Close"][0])
    return stockPrice

def stockPlotter(name2, startDate2, endDate2):
    stockName = yf.Ticker(name2)
    dateList = []
    dateNumbersList = []
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
    #dateNumbersList = range(0, dateListSize)

    fig, ax = plt.subplots()
    plt.plot(dateList, priceList)
    plt.title(name2 + " Performance", fontsize = 20)

    if(dateListSize < 15):
        ax.set_xticks(dateList[::1])
        ax.set_xticklabels(dateList[::1], rotation=90)
    elif(dateListSize < 45):
        ax.set_xticks(dateList[::3])
        ax.set_xticklabels(dateList[::3], rotation=90)
    elif(dateListSize < 90):
        ax.set_xticks(dateList[::6])
        ax.set_xticklabels(dateList[::6], rotation=90)
    elif (dateListSize < 180):
        ax.set_xticks(dateList[::12])
        ax.set_xticklabels(dateList[::12], rotation=90)
    elif (dateListSize < 1825):
        ax.set_xticks(dateList[::60])
        ax.set_xticklabels(dateList[::60], rotation=90)
    elif (dateListSize < 3650):
        ax.set_xticks(dateList[::180])
        ax.set_xticklabels(dateList[::180], rotation=90)
    else:
        ax.set_xticks(dateList[::365])
        ax.set_xticklabels(dateList[::365], rotation=90)

    print (dateList)
    print (priceList)

    plt.xlabel('Date', fontsize = 12)
    #plt.xticks(rotation = 90)
    plt.ylabel('Price ($)', fontsize = 12)
    plt.gcf().subplots_adjust(bottom=0.25)
    #plt.show()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_imageS


def isStockReal(stock):
    stockName = yf.Ticker("AMZN")
    stockDataTable = stockName.history(start = "2020-02-07")
    if not(stockDataTable.empty):
        return True
    else:
        return False



#print(stockPriceCalculator(stock, investAmount, investmentDate, compareDate))
#stockPlotter("AMZN", "2000-02-03", "2020-02-07")
