import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info
msft = msft.history(start="2020-02-03", end="2020-02-05")
print(msft)
