from binance.client import Client
from client import TimeServer
import get_timeserver

# Generate api 'key' and 'secret' as objects to be placed inside client method
api_key = "2Qd7yffVm6t4SCnK2NY4yYvWyZOgpxihnbQy7RnLRCiRsvdB5l9G29rZNPpCoiXG"
api_secret = "REzOpeI2XBNiT7w7ZBkCBVPpAaVAorq7vQaMOyGpy2BPksUGo3ZoxZPV5LKlvCrk"

def client_connect(api_key,api_secret):
    api_key = ""
    api_secret = ""
    client = Client(api_key,api_secret, tld='us')
    TimeServer(api_key,api_secret)


client_connect(api_key,api_secret)