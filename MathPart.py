import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import io

from datetime import datetime
#matplotlib.use('agg')
def stockPriceCalculator(firstStockName, secondStockName, thirdStockName, initAmount, startDate, endDate):
    numOfStocks1 = 0
    initInvestment = 0.00
    initStockPrice1 = 0.00
    endStockPrice1 = 0.00
    endValueOfInvestment1 = 0.00
    investmentGain1 = 0.00
    percentageGain1 = 0.00

    numStocks2 = 0
    initStockPrice2 = 0.00
    endStockPrice2 = 0.00
    endValueOfInvestment2 = 0.00
    investmentGain2 = 0.00
    percentageGain2 = 0.00

    numStocks3 = 0
    initStockPrice3 = 0.00
    endStockPrice3 = 0.00
    endValueOfInvestment3 = 0.00
    investmentGain3 = 0.00
    percentageGain3 = 0.00

    initStockPrice1 = stockPriceLocator(firstStockName, startDate)
    endStockPrice1 = stockPriceLocator(firstStockName, endDate)

    initStockPrice2 = stockPriceLocator(secondStockName, startDate)
    endStockPrice2 = stockPriceLocator(secondStockName, endDate)

    initStockPrice3 = stockPriceLocator(thirdStockName, startDate)
    endStockPrice3 = stockPriceLocator(thirdStockName, endDate)

    numOfStocks1 = int(initAmount/initStockPrice1)
    startInfo1 = "The value of the first stock on " + startDate + " was $" + str(initStockPrice1)

    numOfStocks2 = int(initAmount/initStockPrice2)
    startInfo2 = "The value of the second stock on " + startDate + " was $" + str(initStockPrice2)

    numOfStocks3 = int(initAmount/initStockPrice3)
    startInfo3 = "The value of the third stock on " + startDate + " was $" + str(initStockPrice3)

    if (numOfStocks1 <= 0):
        print("You were not able to buy any stocks for the first stock with your initial investment. Please enter a new amount: ")
        return False

    if (numOfStocks2 <= 0):
        print("You were not able to buy any stocks for the second stock with your initial investment. Please enter a new amount: ")
        return False

    if (numOfStocks3 <= 0):
        print("You were not able to buy any stocks for the third stock with your initial investment. Please enter a new amount: ")
        return False

    initInvestment = round((numOfStocks1 * initStockPrice1), 2)
    buyInfo1 = "You were able to buy " + str(numOfStocks1) + " stocks at $" + str(initInvestment)

    initInvestment = round((numOfStocks2 * initStockPrice2), 2)
    buyInfo2 = "You were able to buy " + str(numOfStocks2) + " stocks at $" + str(initInvestment)

    initInvestment = round((numOfStocks3 * initStockPrice3), 2)
    buyInfo3 = "You were able to buy " + str(numOfStocks3) + " stocks at $" + str(initInvestment)

    endValueOfInvestment1 = round((numOfStocks1 * endStockPrice1), 2)
    endStockInfo1 = "The value of the first stock on " + endDate + " was $" + str(endStockPrice1)
    endInvestmentInfo1 = "The value of your investment in the first stock on " + endDate + " was worth $" + str(endValueOfInvestment1)

    endValueOfInvestment2 = round((numOfStocks2 * endStockPrice2), 2)
    endStockInfo2 = "The value of the second stock on " + endDate + " was $" + str(endStockPrice2)
    endInvestmentInfo2 = "The value of your investment in the second stock on " + endDate + " was worth $" + str(endValueOfInvestment2)

    endValueOfInvestment3 = round((numOfStocks3 * endStockPrice3), 2)
    endStockInfo3 = "The value of the third stock on " + endDate + " was $" + str(endStockPrice3)
    endInvestmentInfo3 = "The value of your investment in the third stock on " + endDate + " was worth $" + str(endValueOfInvestment3)

    investmentGain1 = round((endValueOfInvestment1 - initInvestment), 2)
    percentageGain1 = round(((endValueOfInvestment1 - initInvestment)/initInvestment) * 100, 2)

    investmentGain2 = round((endValueOfInvestment2 - initInvestment), 2)
    percentageGain2 = round(((endValueOfInvestment2 - initInvestment)/initInvestment) * 100, 2)

    investmentGain3 = round((endValueOfInvestment3 - initInvestment), 2)
    percentageGain3 = round(((endValueOfInvestment3 - initInvestment)/initInvestment) * 100, 2)

    if(investmentGain1 < 0):
        investmentGainInfo1 = "Your first investment lost $" + str(investmentGain1)
        percentageGaininfo1 = "That's a " + str(percentageGain1) + "% loss!"
    else:
        investmentGainInfo1 = "Your first investment gained $" + str(investmentGain1)
        percentageGaininfo1 = "That's a " + str(percentageGain1) + "% gain!"

    if(investmentGain2 < 0):
        investmentGainInfo2 = "Your second investment lost $" + str(investmentGain2)
        percentageGaininfo2 = "That's a " + str(percentageGain2) + "% loss!"
    else:
        investmentGainInfo2 = "Your second investment gained $" + str(investmentGain2)
        percentageGaininfo2 = "That's a " + str(percentageGain2) + "% gain!"

    if(investmentGain3 < 0):
        investmentGainInfo3 = "Your third investment lost $" + str(investmentGain3)
        percentageGaininfo3 = "That's a " + str(percentageGain3) + "% loss!"
    else:
        investmentGainInfo3 = "Your third investment gained $" + str(investmentGain3)
        percentageGaininfo3 = "That's a " + str(percentageGain3) + "% gain!"

    returnInfo = {'startInfo1': startInfo1,
                  'buyInfo1': buyInfo1,
                  'endStockInfo1': endStockInfo1,
                  'endInvestmentInfo1': endInvestmentInfo1,
                  'investmentGainInfo1': investmentGainInfo1,
                  'percentageGaininfo1': percentageGaininfo1}

    return (returnInfo)

def stockPriceLocator(stock, date):
    stockPrice = 0.00
    stockName = yf.Ticker(stock)
    stockDataTable = stockName.history(start = date)
    stockPrice = float(stockDataTable["Close"][0])
    return stockPrice

def stockPlotter(firstStockProg, secondStockProg, thirdStockProg, startDate2, endDate2): #Implement multiple names (name1, name2 and name3?)
    stockName1 = yf.Ticker(firstStockProg)
    stockName2 = yf.Ticker(secondStockProg)
    stockName3 = yf.Ticker(thirdStockProg)
    dateList = []
    dateList2 = []
    dateList3 = []
    dateNumbersList = []
    priceList = []
    priceList2 = []
    priceList3 = []
    xTicks = []
    yTicks = []
    dateListSize = 0
    stockDataTable1 = stockName1.history(start = startDate2, end = endDate2)
    stockDataTable2 = stockName2.history(start = startDate2, end = endDate2)
    stockDataTable3 = stockName3.history(start = startDate2, end = endDate2)

    for row in stockDataTable1.itertuples():
        dateString = row.Index.strftime("%Y-%m-%d")
        dateList.append(dateString)
        priceList.append(row.Close)

    for row in stockDataTable2.itertuples():
        dateString = row.Index.strftime("%Y-%m-%d")
        dateList2.append(dateString)
        priceList2.append(row.Close)

    for row in stockDataTable3.itertuples():
        dateString = row.Index.strftime("%Y-%m-%d")
        dateList3.append(dateString)
        priceList3.append(row.Close)

    dateListSize = len(dateList)
    dateNumbersList = range(0, dateListSize)

    fig, ax = plt.subplots()
    plt.plot(dateList, priceList, label = firstStockProg)
    plt.plot(dateList2, priceList2, label = secondStockProg)
    plt.plot(dateList3, priceList3, label = thirdStockProg)
    plt.title(firstStockProg + ", " + secondStockProg + ", and " + thirdStockProg + " Performance", fontsize = 20)
    plt.legend(loc = 'upper left')

    #Is there a way to improve on this code so it's not a bunch of if-else statements?
    #The goal is for PyPlot to be able to display

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

    #print (dateList)
    #print (priceList)

    plt.xlabel('Date', fontsize = 12)
    #plt.xticks(rotation = 90)
    plt.ylabel('Price ($)', fontsize = 12)
    plt.gcf().subplots_adjust(bottom=0.25)
    plt.show()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image


def isStockReal(stock):
    stockName = yf.Ticker(stock)
    stockDataTable = stockName.history(start = "2020-02-07")
    if not(stockDataTable.empty):
        return True
    else:
        return False



#print(stockPriceCalculator(stock, investAmount, investmentDate, compareDate))

stockPlotter("AMZN", "TSLA", "DIS", "2020-01-01", "2020-08-01")
