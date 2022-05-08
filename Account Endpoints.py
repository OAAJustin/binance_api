from binance.client import Client
import pandas as pd

api_key = "2Qd7yffVm6t4SCnK2NY4yYvWyZOgpxihnbQy7RnLRCiRsvdB5l9G29rZNPpCoiXG"
api_secret = "REzOpeI2XBNiT7w7ZBkCBVPpAaVAorq7vQaMOyGpy2BPksUGo3ZoxZPV5LKlvCrk"

client = Client(api_key,api_secret, tld='us')

# Get Account Info
info = client.get_account()
print(info)

for key,value in info.items():
    print("{} : {}".format(key,value))
    
# Get Asset Balance 
balance = client.get_asset_balance(asset='BTC')
print(balance)

for key,value in balance.items():
    print("{} : {}".format(key,value))
    
# Get Account Status - ERROR!
status = client.get_account_status()
print(status)

# Get Account API Trading Status
status_api = client.get_account_api_trading_status()

# Get Asset Details
details = client.get_asset_details()

# 