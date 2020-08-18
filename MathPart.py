import yfinance as yf
from datetime import datetime, date, timedelta
import copy


#class represents stock object with an initial investment amount and start and end dates of investment
class Stock:
    
    def __init__(self, stock_name, init_amount, start_date, end_date, recurring_investment, frequency_of_investments):
        self.stock_name = stock_name
        #how much the user wants to initially invest
        self.init_amount = init_amount
        #cost basis is the amount the user has actually paid for stocks
        self.init_cost_basis = 0
        self.final_cost_basis = 0
        #iso format is "YYYY-MM-DD"
        self.start_date = date.fromisoformat(start_date)
        self.end_date = date.fromisoformat(end_date)
        #Ticker object of the stock the user wants to buy
        self.ticker_info = yf.Ticker(stock_name)
        #amount user wants to invest on a periodic basis
        self.recurring_investment = recurring_investment
        #how often the user wants to invest periodically
        self.frequency_of_investments = frequency_of_investments
        #how many of those periods occur between the start and end date
        self.num_of_recurring_investments = 0
        #list to store all dates between start and end dates
        self.dates = []
        #list to store all prices of the stock between the start and end date
        self.prices = []
        #list to store how much user has invested in stock for all days in the date list
        self.cost_bases = []
        #list to store the dates recurring investments are made
        self.recurring_dates = []
        #list to store the prices of the stocks on the recurring dates
        self.recurring_prices = []
        #list to store the price user has paid for each recurring investment
        self.additions_to_cost_basis = []
        
        #gets price of stock on the start and end dates
        self.init_stock_price = self.stock_price_locator(start_date)
        self.final_stock_price = self.stock_price_locator(end_date)

        #integer number of stocks you can buy
        self.num_of_stocks = init_amount // self.init_stock_price
        self.init_cost_basis = round(self.num_of_stocks * self.init_stock_price, 2)
        self.final_cost_basis = copy.deepcopy(self.init_cost_basis)
        self.final_investment_value = round(self.num_of_stocks * self.final_stock_price, 2)
        self.buy_more_stocks()
        
        #can buy stocks or not
        self.can_buy_stock = True
        if self.num_of_stocks <= 0:
            self.can_buy_stock = False

        self.investment_gain = round(self.final_investment_value - self.final_cost_basis, 2)
        self.percentage_gain = round((self.investment_gain / self.final_cost_basis) * 100, 2)

    #returns price of stock on given date
    def stock_price_locator(self, date):
        stockPrice = 0.00
        stockDataTable = self.ticker_info.history(start=date)
        stockPrice = float(stockDataTable["Close"][0])
        return stockPrice
    
    #fills recurring_dates and recurring_prices list
    def recurring_dates_and_prices_finder(self):
        buy_date = copy.deepcopy(self.start_date)
      
        if(self.frequency_of_investments == "monthly"):
            #number of months between start and end dates
            self.num_of_recurring_investments = (self.end_date - self.start_date).days // 30
            
            for i in range(self.num_of_recurring_investments):
                buy_date = buy_date + timedelta(days=30)
                new_stock_price = self.stock_price_locator(buy_date)
                self.recurring_dates.append(buy_date)
                self.recurring_prices.append(new_stock_price)
                
                
        elif(self.frequency_of_investments == "quarterly"):
            #number of quarters between start and end dates
            self.num_of_recurring_investments = (self.end_date - self.start_date).days // 91

            for i in range(self.num_of_recurring_investments):
                buy_date = buy_date + timedelta(days=91)
                new_stock_price = self.stock_price_locator(buy_date)
                self.recurring_dates.append(buy_date)
                self.recurring_prices.append(new_stock_price)

        elif(self.frequency_of_investments == "biyearly"):
            #number half year periods between start and end date
            self.num_of_recurring_investments = (self.end_date - self.start_date).days // 182
            
            for i in range(self.num_of_recurring_investments):
                buy_date = buy_date + timedelta(days=182)
                new_stock_price = self.stock_price_locator(buy_date)
                self.recurring_dates.append(buy_date)
                self.recurring_prices.append(new_stock_price)

        elif(self.frequency_of_investments == "yearly"):
            #number of years between start and end date
            self.num_of_recurring_investments = (self.end_date - self.start_date).days // 362
            
            for i in range(self.num_of_recurring_investments):
                buy_date = buy_date + timedelta(days=365)
                new_stock_price = self.stock_price_locator(buy_date)
                self.recurring_dates.append(buy_date)
                self.recurring_prices.append(new_stock_price)

    #adds to num_of_stocks and cost_basis attributes
    def buy_more_stocks(self):

        for i in range(self.num_of_recurring_investments):
            #num of stocks user can buy with recurring investment amount
            recurring_investment_stocks = self.recurring_investment // self.recurring_prices[i]
            self.num_of_stocks += recurring_investment_stocks
            #amount user has paid for recurring investment
            recurring_investment_price = round(recurring_investment_stocks * self.recurring_prices[i], 2)
            self.additions_to_cost_basis.append(recurring_investment_price)
            self.final_cost_basis += recurring_investment_price
    
    #fills dates list
    def get_dates(self):
        time_diff = (self.end_date - self.start_date).days
        first_date = copy.deepcopy(self.start_date)
        for i in range(time_diff):    
            first_date_string = str(first_date)
            self.dates.append(first_date_string)
            first_date += timedelta(days=1)

    #fills prices list
    def get_prices(self):
        for i in range(len(self.dates)):
            date = self.dates[i]    
            price = self.stock_price_locator(date)
            self.prices.append(price)

    #fills cost_bases list
    #will result in a "stair-step" looking trace
    def get_invested_amounts(self):
        idx = 0
        running_cost_basis = copy.deepcopy(self.init_cost_basis)
        for i in range(len(self.dates)):
            #checks if date is a recurring investment date
            if self.dates[i] in self.recurring_dates:
                running_cost_basis += self.additions_to_cost_basis[idx]
                idx += 1
            #if date was not a recurring investment date, cost basis will not have changed
            self.cost_bases.append(running_cost_basis)


    def info_print_out(self):
        
        if(self.investment_gain >= 0):
            self.investment_gain_info = "Your investment gained $" + str(self.investment_gain)
        else:
            self.investment_gain_info = "Your investment lost $" + str(self.investment_gain)

        if(self.investment_gain >= 0):
            self.percentage_gain_info = "That's a  %" + str(self.percentage_gain) + " gain !"
        else:
            self.percentage_gain_info = "That's a  %" + str(self.percentage_gain) + " loss !"
        
        return {'Start Info': "The value of " + self.stock_name + " on " + str(self.start_date) + " was $" + str(self.init_stock_price),
         'Buy Info': "You were able to buy " + str(self.num_of_stocks) + " shares at $" + str(self.final_cost_basis),
         'Final Info': "The value of " + self.stock_name + " on " + str(self.end_date) + " was $" + str(self.final_stock_price),
         'End Investment Info': "The value of your investment on " + str(self.end_date) + " was worth $" + str(self.final_investment_value),
         'Investment Gain info': self.investment_gain_info,
         'Percentage Gain Info': self.percentage_gain_info}

#class aggregates stock objects
class  Portfolio():
    def __init__(self, *args):
        self.stocks = []
        #final cost basis of entire portfolio
        self.tot_cost_basis = 0
        self.start_date = args[0].start_date
        self.end_date = args[0].end_date
        self.tot_recurring_investment = 0
        #value of entire portfolio on the end date
        self.tot_end_value = 0
        self.tot_gain = 0
        #stores the values of the portfolio on every day between the start and end date
        self.values_of_portfolio = []
        #stores the cost bases on every day between the start and end date
        self.cost_bases = []

        for stock in args:
            self.stocks.append(stock)
        
        for stock in args:
            self.tot_cost_basis += stock.cost_basis
        self.tot_cost_basis = round(self.tot_cost_basis, 2)
        
        for stock in args:
            self.tot_recurring_investment += stock.recurring_investment
        
        for stock in args:
            self.tot_end_value += stock.final_investment_amount

        for stock in args:
            self.tot_gain += stock.investment_gain
        
        self.tot_percentage_gain = round((self.tot_gain / self.tot_cost_basis) * 100, 2)

    def get_values_and_cost_bases(self):
        #outer loop iterates over the length of the dates/prices/cost bases list of every stock in the portfolio
        for i in range(len(self.stocks[0].dates)):
            #inner loop iterates over every stock in the portfolio
            for stock in self.stocks:
                cost_basis += stock.cost_bases[i]
                value += stock.prices[i]
            self.cost_bases.append(cost_basis)
            self.values_of_portfolio.append(value)
    
    def info_print_out(self):
        
        if(self.tot_gain >= 0):
            self.tot_gain_info = "Your portfolio gained $" + str(self.tot_gain)
        else:
            self.tot_gain_info = "Your portfolio lost $" + str(self.tot_gain)

        if(self.tot_percentage_gain >= 0):
            self.percentage_gain_info = "That's a  %" + str(self.tot_percentage_gain) + " gain !"
        else:
            self.percentage_gain_info = "That's a  %" + str(self.tot_percentage_gain) + " loss !"
        
        return {'Start Info': "The value of your portfolio on " + str(self.start_date) + " was $" + str(self.tot_cost_basis),
            'Final Info': "The value of your portfolio on " + str(self.end_date) + " was $" + str(self.tot_end_value),
            'Investment Gain info': self.tot_gain_info,
            'Percentage Gain Info': self.percentage_gain_info}



'''
class StockPlotter:

    def __init__(self, *args):
        
        matplotlib.use('agg')
        fig, ax = plt.subplots()
        graph_title = ""
        date_list = []
        first_stock_data_table = args[0].ticker_info.history(start = args[0].start_date, end = args[0].end_date)

        for row in first_stock_data_table.itertuples():
            date_string = row.Index.strftime("%Y-%m-%d")
            date_list.append(date_string)
        
        date_list_size = len(date_list)

        for stock in args:
            
            stock_ticker = stock.ticker_info
            price_list = []
            stock_data_table = stock_ticker.history(start = stock.start_date, end = stock.end_date)

            for row in stock_data_table.itertuples():
                price_list.append(row.Close)
            
            

            plt.plot(date_list, price_list, label = stock.stock_name)
            graph_title += stock.stock_name + ", "

        
        plt.legend(loc = 'upper left')

        #Is there a way to improve on this code so it's not a bunch of if-else statements?
        #The goal is for PyPlot to be able to display

        if(date_list_size < 15):
            ax.set_xticks(date_list[::1])
            ax.set_xticklabels(date_list[::1], rotation=90)
        elif(date_list_size < 45):
            ax.set_xticks(date_list[::3])
            ax.set_xticklabels(date_list[::3], rotation=90)
        elif(date_list_size < 90):
            ax.set_xticks(date_list[::6])
            ax.set_xticklabels(date_list[::6], rotation=90)
        elif (date_list_size < 180):
            ax.set_xticks(date_list[::12])
            ax.set_xticklabels(date_list[::12], rotation=90)
        elif (date_list_size < 1825):
            ax.set_xticks(date_list[::60])
            ax.set_xticklabels(date_list[::60], rotation=90)
        elif (date_list_size < 3650):
            ax.set_xticks(date_list[::180])
            ax.set_xticklabels(date_list[::180], rotation=90)
        else:
            ax.set_xticks(date_list[::365])
            ax.set_xticklabels(date_list[::365], rotation=90)
        #print (date_list)
        #print (priceList)

        plt.xlabel('Date', fontsize = 12)
        #plt.xticks(rotation = 90)
        plt.ylabel('Price ($)', fontsize = 12)
        plt.gcf().subplots_adjust(bottom=0.25)
        # plt.show()
        self.bytes_image = io.BytesIO()
        plt.savefig(self.bytes_image, format='png')
        self.bytes_image.seek(0)
    
    def graph_return(self):
        return self.bytes_image

'''
        

        
'''
def stockPlotter(firstStockProg, secondStockProg, thirdStockProg, startDate2, endDate2): #Implement multiple names (name1, name2 and name3?)
    stockName1 = yf.Ticker(firstStockProg)
    stockName2 = yf.Ticker(secondStockProg)
    stockName3 = yf.Ticker(thirdStockProg)
    date_list = []
    date_list2 = []
    date_list3 = []
    dateNumbersList = []
    priceList = []
    priceList2 = []
    priceList3 = []
    xTicks = []
    yTicks = []
    date_list_size = 0
    stockDataTable1 = stockName1.history(start = startDate2, end = endDate2)
    stockDataTable2 = stockName2.history(start = startDate2, end = endDate2)
    stockDataTable3 = stockName3.history(start = startDate2, end = endDate2)

    for row in stockDataTable1.itertuples():
        dateString = row.Index.strftime("%Y-%m-%d")
        date_list.append(dateString)
        priceList.append(row.Close)

    for row in stockDataTable2.itertuples():
        dateString = row.Index.strftime("%Y-%m-%d")
        date_list2.append(dateString)
        priceList2.append(row.Close)

    for row in stockDataTable3.itertuples():
        dateString = row.Index.strftime("%Y-%m-%d")
        date_list3.append(dateString)
        priceList3.append(row.Close)

    date_list_size = len(date_list)

    fig, ax = plt.subplots()
    plt.plot(date_list, priceList, label = firstStockProg)
    plt.plot(date_list2, priceList2, label = secondStockProg)
    plt.plot(date_list3, priceList3, label = thirdStockProg)
    plt.title(firstStockProg + ", " + secondStockProg + ", and " + thirdStockProg + " Performance", fontsize = 20)
    plt.legend(loc = 'upper left')

    #Is there a way to improve on this code so it's not a bunch of if-else statements?
    #The goal is for PyPlot to be able to display

    if(date_list_size < 15):
        ax.set_xticks(date_list[::1])
        ax.set_xticklabels(date_list[::1], rotation=90)
    elif(date_list_size < 45):
        ax.set_xticks(date_list[::3])
        ax.set_xticklabels(date_list[::3], rotation=90)
    elif(date_list_size < 90):
        ax.set_xticks(date_list[::6])
        ax.set_xticklabels(date_list[::6], rotation=90)
    elif (date_list_size < 180):
        ax.set_xticks(date_list[::12])
        ax.set_xticklabels(date_list[::12], rotation=90)
    elif (date_list_size < 1825):
        ax.set_xticks(date_list[::60])
        ax.set_xticklabels(date_list[::60], rotation=90)
    elif (date_list_size < 3650):
        ax.set_xticks(date_list[::180])
        ax.set_xticklabels(date_list[::180], rotation=90)
    else:
        ax.set_xticks(date_list[::365])
        ax.set_xticklabels(date_list[::365], rotation=90)

    #print (date_list)
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

'''


if __name__ == "__main__":
    disney_stock = Stock("DIS", 5000, "2020-01-06", "2020-03-01", 0, "none")
    apple_stock = Stock("AAPL", 5000, "2020-01-06", "2020-03-01", 0, "none")
    portfolio = Portfolio(disney_stock, apple_stock)

    disney_stock.get_dates()

    print(disney_stock.dates)