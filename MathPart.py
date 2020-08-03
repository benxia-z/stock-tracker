import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import io

from datetime import datetime
#matplotlib.use('agg')

#class represents stock object with an initial investment amount and start and end dates of investment
amazon_stock = Stock('AMZN', 1000, '2010-01-01', '2020-01-01')
amazon_stock.info_print_out()
info_print_out()

class Stock:
    
    def __init__(self, stock_name, init_amount, start_date, end_date):
        
        self.stock_name = stock_name
        self.init_amount = init_amount
        self.start_date = start_date
        self.end_date = end_date
        
        #gets price of stock on the start and end dates
        self.init_stock_price = self.stock_price_locator(stock_name, start_date)
        self.final_stock_price = self.stock_price_locator(stock_name, end_date)

        #integer number of stocks you can buy
        self.num_of_stocks = init_amount // self.init_stock_price
        
        #can buy stocks or not
        self.can_buy_stock = True
        if self.num_of_stocks <= 0:
            self.can_buy_stock = False

        self.init_investment_amount = round(self.num_of_stocks * self.init_stock_price, 2)
        self.final_investment_amount = round(self.num_of_stocks * self.final_stock_price, 2)

        self.investment_gain = round(self.final_investment_amount - self.init_investment_amount, 2)
        self.percentage_gain = round((self.investment_gain / self.init_investment_amount) * 100, 2)

    def stock_price_locator(self, stock, date):
        stockPrice = 0.00
        stockName = yf.Ticker(stock)
        stockDataTable = stockName.history(start = date)
        stockPrice = float(stockDataTable["Close"][0])
        return stockPrice
    
    def info_print_out(self):
        
        if(self.investment_gain >= 0):
            self.investment_gain_info = "Your investment gained $" + str(self.investment_gain)
        else:
            self.investment_gain_info = "Your investment lost $" + str(self.investment_gain)

        if(self.investment_gain >= 0):
            self.percentage_gain_info = "That's a  %" + self.percentage_gain + "gain !"
        else:
            self.percentage_gain_info = "That's a  %" + self.percentage_gain + "loss !"
        
        {'Start Info': "The value of " + self.stock_name + " on " + self.start_date + " was $" + str(self.init_stock_price),
         'Buy Info': "You were able to buy " + str(self.num_of_stocks) + " shares at $" + str(self.init_investment_amount),
         'Final Info': "The value of " + self.stock_name + " on " + self.end_date + " was $" + str(self.final_stock_price),
         'End Investment Info': "The value of your investment on " + self.end_date + " was worth $" + str(self.final_investment_amount),
         'Investment Gain info': self.investment_gain_info,
         'Percentage Gain Info': self.percentage_gain_info}
        
        
        
        self.endStockPrice = 0.00
        self.endValueOfInvestment = 0.00
        self.investmentGain = 0.00
        self.percentageGain = 0.00

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
