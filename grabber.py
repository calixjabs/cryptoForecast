#!/usr/bin/python3

##
## run the code for about 2/3 days
##

import requests
import time

f_name = input("dataset name:")
f = open(f_name,"a")
keys = ["price_usd","24h_volume_usd","market_cap_usd","available_supply","total_supply","percent_change_1h","percent_change_24h","percent_change_7d"]
vals = [0]*len(keys)

while True:
  data = requests.get("https://api.coinmarketcap.com/v1/ticker/neo/").json()[0]
  coincap = requests.get("http://coincap.io/page/NEO").json() 
  bittrex = requests.get("https://bittrex.com/api/v1.1/public/getticker?market=usdt-neo").json()
  
  for d in data.keys():
     if d in keys:
       indx = keys.index(d)
       vals[indx] = data[d]
  for val in vals:
       f.write(val+",")
      
  f.write("{},{},".format(coincap["volume"],coincap["vwap_h24"]))
  f.write("{},{},{}".format(bittrex["result"]["Bid"],bittrex["result"]["Ask"],bittrex["result"]["Last"]))
  f.write("\n")
  f.flush()
  time.sleep(9*60)
