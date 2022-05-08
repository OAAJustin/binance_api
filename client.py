# Import Dependencies
from binance.client import Client
import pandas as pd
from datetime import datetime
import time
import json

# Generate api 'key' and 'secret' as objects to be placed inside client method
api_key = "2Qd7yffVm6t4SCnK2NY4yYvWyZOgpxihnbQy7RnLRCiRsvdB5l9G29rZNPpCoiXG"
api_secret = "REzOpeI2XBNiT7w7ZBkCBVPpAaVAorq7vQaMOyGpy2BPksUGo3ZoxZPV5LKlvCrk"

# Connect to the Client - Does NOT contain TLD
client = Client(api_key,api_secret) 

# Connect to the Client using TestNet -  Does NOT contain TLD
client = Client(api_key,api_secret, testnet=True)

# Connect to the Client using TestNet - Does contain TLD
client = Client(api_key,api_secret, testnet=True, tld='us')

# Connect to the Client - Does contain TLD
client = Client(api_key,api_secret, tld='us')

# Get all Coin's Tickers'
tickers = client.get_all_tickers()
df = pd.DataFrame(tickers)
print(df.set_index("price").sort_values(by=["price"]).to_markdown())
print(df.to_markdown())

# Ping the Server
client.ping()

# Get the Server Time
TimeServer = client.get_server_time()
print(TimeServer)
    
# Repleace Single Quotes with Double Quotes   
stime = TimeServer
TimeServerStr = str(stime).replace("'",'"')
data = json.loads(TimeServerStr)
print(data)
print(type(data))
print(data['serverTime'])

# Print Server Time as Integer
TimeServerInt = print(int(data['serverTime']))

# Print Server Time as Time Structure as GMT
TimeServerT = time.strftime("%X",time.gmtime(TimeServerInt))

# Function to Return Server Time in GMT
def TimeServer(api_key,api_secret):
    api_key = ""
    api_secret = ""
    client = Client(api_key,api_secret, tld='us')
    TimeServer = client.get_server_time()
    stime = TimeServer
    TimeServerStr = str(stime).replace("'",'"')
    data = json.loads(TimeServerStr)
    TimeServerInt = print(int(data['serverTime']))
    TimeServerT = time.strftime("%X",time.gmtime(TimeServerInt))
    print("Server Time (GMT): " + TimeServerT)
    
TimeServer(api_key,api_secret)
    
# Get System Status
status = client.get_system_status()
print(status)

# Get Exchange Info
info = client.get_exchange_info()
print(info)

# Get Symbol Info
InfoSymbol = client.get_symbol_info("SOLUSD")
for key,value in InfoSymbol.items():
    print("{} : {}".format(key,value))
    
# Get Symbol Info
def InfoSymbol(symbol):
    InfoSymbol = client.get_symbol_info(symbol)
    for key,value in InfoSymbol.items():
        print("{} : {}".format(key,value))