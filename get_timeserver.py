from binance.client import Client

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