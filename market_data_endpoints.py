from binance.client import Client
from numpy import int64
import pandas as pd
import time

client = Client(api_key,api_secret, tld='us')

# Get Market Depth
depth = client.get_order_book(symbol='BTCUSD')
depth_df = pd.DataFrame(depth)
depth_df.to_csv("btc_depth.csv")
depth_df.head()

# Get Recent Trades
trades = client.get_recent_trades(symbol='BTCUSD')

# Convert Results into a Data Frame
trades_df = pd.DataFrame(trades)

# Show top 5 entries
trades_df.head()

# Set the Index to the "ID" column
trades_df.set_index("id")

# Show Info to display the DTypes
trades_df.info()

# Convert Columns from Object to Float64
trades_df["price"] = pd.to_numeric(trades_df["price"])
trades_df["qty"] = pd.to_numeric(trades_df["qty"])
trades_df["quoteQty"] = pd.to_numeric(trades_df["quoteQty"])

# Show Info to display the DTypes after conversion
trades_df.info()

print(trades_df.to_markdown())

# Get Aggregate Trades 
agg_trades = client.get_historical_trades(symbol="BTCUSD")
print(agg_trades)
agg_trades_df = pd.DataFrame(agg_trades)
agg_trades_df.head()

# Get Kline/Candlesticks
candles = client.get_klines(symbol="BTCUSD", interval = client.KLINE_INTERVAL_30MINUTE)
print(candles)
candles_df = pd.DataFrame(candles)
candles_df.head()

# Get Average Price for a Symbol
avg_price = client.get_avg_price(symbol="BTCUSD",)
print(avg_price)

# Get 24hr Ticker
tickers = client.get_ticker()
print(tickers)
tickers_df = pd.DataFrame(tickers)
print(tickers_df)

# Get All Prices 
prices = client.get_all_tickers()
print(prices)
prices_df = pd.DataFrame(prices)
print(prices_df)
print(prices_df.to_markdown())

# Get Orderbook Tickers
tickers = client.get_orderbook_tickers()
print(tickers)
tickers_df = pd.DataFrame(tickers)
print(tickers_df)