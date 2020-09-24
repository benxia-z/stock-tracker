import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info
msft_history = msft.history(start="2020-02-03", end = "2020-03-03")
print(msft_history)
